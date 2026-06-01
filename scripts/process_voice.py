#!/usr/bin/env python3
"""
process_voice.py — обработка голосовых сообщений из Telegram для Obsidian/Logseq vault.

Использование:
    python process_voice.py audio.ogg
    python process_voice.py audio.ogg --date 2026-06-02 --dry-run
    python process_voice.py audio.ogg --model small --lang en
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Dependency checks
# ---------------------------------------------------------------------------

def check_ffmpeg() -> None:
    """Raise SystemExit with a helpful message if ffmpeg is not in PATH."""
    result = subprocess.run(
        ["ffmpeg", "-version"],
        capture_output=True,
    )
    if result.returncode != 0:
        sys.exit(
            "Error: ffmpeg not found in PATH.\n"
            "Install it with:  sudo apt install ffmpeg  (Debian/Ubuntu)\n"
            "                  sudo dnf install ffmpeg  (Fedora/RHEL)"
        )


def import_faster_whisper():
    """Import faster_whisper or exit with a helpful message."""
    try:
        from faster_whisper import WhisperModel  # noqa: PLC0415
        return WhisperModel
    except ImportError:
        sys.exit(
            "Error: faster-whisper is not installed.\n"
            "Install it with:  pip install faster-whisper"
        )


# ---------------------------------------------------------------------------
# Audio processing
# ---------------------------------------------------------------------------

RNNOISE_MODEL = "rnnoise-models/somnolent-hogwash-2018-09-01.rnnn"


def build_audio_filter(use_rnnoise: bool) -> str:
    """Return the ffmpeg -af filter chain string."""
    filters = []

    # Silence removal at start/end
    filters.append("silenceremove=start_periods=1:start_threshold=-50dB"
                   ":stop_periods=-1:stop_threshold=-50dB:stop_duration=0.5")

    # Noise reduction — prefer arnndn, fall back to highpass+afftdn
    if use_rnnoise:
        filters.append(f"arnndn=m={RNNOISE_MODEL}")
    else:
        filters.append("highpass=f=80")
        filters.append("afftdn=nf=-25")

    # Loudness normalisation (EBU R128)
    filters.append("loudnorm")

    return ",".join(filters)


def convert_to_wav(input_path: Path, output_path: Path) -> None:
    """Convert *input_path* to a 16 kHz mono WAV at *output_path* via ffmpeg."""
    use_rnnoise = Path(RNNOISE_MODEL).exists()
    af = build_audio_filter(use_rnnoise)

    cmd = [
        "ffmpeg",
        "-y",                    # overwrite without asking
        "-i", str(input_path),
        "-ar", "16000",          # 16 kHz sample rate required by Whisper
        "-ac", "1",              # mono
        "-af", af,
        str(output_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(
            f"Error: ffmpeg conversion failed.\n"
            f"Command: {' '.join(cmd)}\n"
            f"stderr:\n{result.stderr}"
        )


# ---------------------------------------------------------------------------
# Transcription
# ---------------------------------------------------------------------------

def transcribe(wav_path: Path, model_size: str, language: str) -> str:
    """Run faster-whisper on *wav_path* and return the plain-text transcript."""
    WhisperModel = import_faster_whisper()

    print(f"[whisper] Loading model '{model_size}' (device=cpu, compute_type=int8)…",
          file=sys.stderr)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, _info = model.transcribe(
        str(wav_path),
        language=language,
        beam_size=5,
    )

    parts = [seg.text.strip() for seg in segments if seg.text.strip()]
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Routing logic
# ---------------------------------------------------------------------------

# Patterns that trigger routing away from the daily journal
_TAG_PATTERNS = {
    "person":   re.compile(r"#(?:person|человек)\s+(\S+)", re.IGNORECASE),
    "project":  re.compile(r"#(?:project|проект)\s+(\S+)", re.IGNORECASE),
    "finance":  re.compile(r"#(?:fin|финансы)\b", re.IGNORECASE),
}


def route(transcript: str, vault: Path, date: datetime) -> tuple[Path, str]:
    """
    Determine the target file and section header for *transcript*.

    Returns (target_path, mode) where mode is 'append' (always for now).
    """
    # --- person ---
    m = _TAG_PATTERNS["person"].search(transcript)
    if m:
        name = m.group(1).strip("#,. ")
        if name:
            target = vault / "pages" / f"{name}.md"
        else:
            target = vault / "pages" / "voice-notes.md"
        return target, "append"

    # --- project ---
    m = _TAG_PATTERNS["project"].search(transcript)
    if m:
        name = m.group(1).strip("#,. ")
        target = vault / "projects" / f"{name}.md"
        return target, "append"

    # --- finance ---
    if _TAG_PATTERNS["finance"].search(transcript):
        target = vault / "pages" / "Expenses.md"
        return target, "append"

    # --- default: daily journal ---
    year = date.strftime("%Y")
    day  = date.strftime("%Y-%m-%d")
    target = vault / "journals" / year / f"{day}.md"
    return target, "append"


# ---------------------------------------------------------------------------
# File writing
# ---------------------------------------------------------------------------

def format_entry(transcript: str, timestamp: datetime) -> str:
    """Return the Logseq-outline formatted entry string."""
    time_str = timestamp.strftime("%H:%M")
    return f"- 🎙️ [{time_str}] голосовое\n  - {transcript}\n"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def append_to_file(path: Path, entry: str) -> None:
    ensure_parent(path)
    # Ensure file ends with newline before appending
    if path.exists() and path.stat().st_size > 0:
        with open(path, "rb") as fh:
            fh.seek(-1, 2)
            last_byte = fh.read(1)
        if last_byte != b"\n":
            with open(path, "a", encoding="utf-8") as fh:
                fh.write("\n")
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(entry)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe a voice message and append it to the Obsidian/Logseq vault.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("audio", type=Path, help="Path to the input audio file (OGG/MP3/WAV).")
    parser.add_argument(
        "--vault", type=Path, default=Path("/home/rocky/logseq-content"),
        help="Path to the Obsidian/Logseq vault (default: /home/rocky/logseq-content).",
    )
    parser.add_argument(
        "--date", type=str, default=None,
        metavar="YYYY-MM-DD",
        help="Date for the journal entry (default: today).",
    )
    parser.add_argument(
        "--model", type=str, default="base",
        choices=["tiny", "base", "small", "medium", "large-v2", "large-v3"],
        help="Whisper model size (default: base).",
    )
    parser.add_argument(
        "--lang", type=str, default="ru",
        help="Language code for transcription (default: ru).",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print the result without writing to any file.",
    )
    parser.add_argument(
        "--keep-wav", action="store_true",
        help="Keep the temporary WAV file after processing.",
    )
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)

    # Validate inputs
    if not args.audio.exists():
        sys.exit(f"Error: audio file not found: {args.audio}")

    check_ffmpeg()

    # Resolve date
    if args.date:
        try:
            entry_date = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            sys.exit(f"Error: invalid date '{args.date}', expected YYYY-MM-DD.")
    else:
        entry_date = datetime.now()

    # Convert to WAV
    tmp_dir = tempfile.mkdtemp(prefix="voice_")
    wav_path = Path(tmp_dir) / "audio.wav"

    print(f"[ffmpeg] Converting {args.audio} → {wav_path} …", file=sys.stderr)
    convert_to_wav(args.audio, wav_path)

    try:
        # Transcribe
        transcript = transcribe(wav_path, args.model, args.lang)
        if not transcript:
            print("Warning: transcription returned an empty string.", file=sys.stderr)
            transcript = "(пусто)"

        print(f"[transcript]\n{transcript}\n", file=sys.stderr)

        # Route
        target_path, _mode = route(transcript, args.vault, entry_date)
        entry = format_entry(transcript, entry_date)

        print(f"[target] {target_path}", file=sys.stderr)
        print(f"[entry]\n{entry}", file=sys.stderr)

        if args.dry_run:
            print("--- DRY RUN — nothing written ---")
            print(f"Target: {target_path}")
            print(f"Entry:\n{entry}")
        else:
            append_to_file(target_path, entry)
            print(f"Appended to {target_path}")

    finally:
        if not args.keep_wav:
            wav_path.unlink(missing_ok=True)
            try:
                Path(tmp_dir).rmdir()
            except OSError:
                pass
        else:
            print(f"[keep-wav] WAV file kept at: {wav_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
