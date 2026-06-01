#!/usr/bin/env python3
"""
Inventory all ((uuid)) block-refs in logseq-content pages.

Reads:  /home/rocky/logseq-content/pages/*.md  (read-only)
Output: data/block_refs.json  — {uuid: {file, line, text}}
        data/block_refs.md    — human-readable summary

Usage:
    python3 scripts/inventory_block_refs.py
    python3 scripts/inventory_block_refs.py --source /path/to/pages --unresolved
"""

import argparse
import json
import re
import sys
from pathlib import Path

BLOCK_REF_RE = re.compile(r"\(\(([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\)\)")
BLOCK_ID_RE  = re.compile(r"^[\t ]*(?:-\s+)?id::\s*([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\s*$")

_REPO = Path(__file__).parent.parent


def build_id_map(pages_dir: Path) -> dict:
    """Map uuid → {file, line, text} for all blocks with id:: property."""
    id_map = {}
    for md in sorted(pages_dir.glob("*.md")):
        lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            m = BLOCK_ID_RE.match(line)
            if m:
                uuid = m.group(1)
                text = lines[i - 1].strip().lstrip("- ") if i > 0 else ""
                id_map[uuid] = {"file": md.name, "line": i + 1, "text": text[:120]}
    return id_map


def find_refs(pages_dir: Path) -> list:
    """Find all ((uuid)) references with their location."""
    refs = []
    for md in sorted(pages_dir.glob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            for m in BLOCK_REF_RE.finditer(line):
                refs.append({"ref_file": md.name, "ref_line": i, "uuid": m.group(1),
                              "context": line.strip()[:100]})
    return refs


def main():
    parser = argparse.ArgumentParser(description="Inventory Logseq block-refs ((uuid))")
    parser.add_argument("--source", default=str(_REPO / "data/pages"),
                        help="Path to pages directory")
    parser.add_argument("--unresolved", action="store_true",
                        help="Show only unresolved refs (no matching id::)")
    parser.add_argument("--output", default=str(_REPO / "data"),
                        help="Output directory for JSON and MD reports")
    args = parser.parse_args()

    pages_dir = Path(args.source)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Scanning {pages_dir} …")
    id_map = build_id_map(pages_dir)
    refs   = find_refs(pages_dir)

    print(f"  Block IDs found:  {len(id_map)}")
    print(f"  Block refs found: {len(refs)}")

    resolved   = [r for r in refs if r["uuid"] in id_map]
    unresolved = [r for r in refs if r["uuid"] not in id_map]
    print(f"  Resolved:   {len(resolved)}")
    print(f"  Unresolved: {len(unresolved)}")

    # Enrich resolved refs
    for r in resolved:
        r.update(id_map[r["uuid"]])

    report = refs if not args.unresolved else unresolved

    # JSON
    json_path = output_dir / "block_refs.json"
    json_path.write_text(json.dumps({"id_map": id_map, "refs": report}, ensure_ascii=False, indent=2))
    print(f"\nJSON → {json_path}")

    # Markdown summary
    md_lines = [
        "# Инвентаризация block-refs",
        "",
        f"- Всего `((uuid))` ссылок: **{len(refs)}**",
        f"- Разрешено (есть `id::`): **{len(resolved)}**",
        f"- Не разрешено: **{len(unresolved)}**",
        "",
        "## Неразрешённые ссылки",
        "",
        "| Файл | Строка | UUID | Контекст |",
        "|------|--------|------|----------|",
    ]
    for r in unresolved[:50]:
        md_lines.append(f"| {r['ref_file']} | {r['ref_line']} | `{r['uuid'][:8]}…` | {r['context']} |")
    if len(unresolved) > 50:
        md_lines.append(f"| … | | | *(ещё {len(unresolved)-50})* |")

    md_lines += [
        "",
        "## Разрешённые ссылки",
        "",
        "| Откуда | Стр. | → Файл | Стр. | Текст блока |",
        "|--------|------|--------|------|-------------|",
    ]
    for r in resolved[:100]:
        md_lines.append(
            f"| {r['ref_file']} | {r['ref_line']} | {r.get('file','')} | {r.get('line','')} | {r.get('text','')} |"
        )
    if len(resolved) > 100:
        md_lines.append(f"| … | | | | *(ещё {len(resolved)-100})* |")

    md_path = output_dir / "block_refs.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print(f"Markdown → {md_path}")


if __name__ == "__main__":
    main()
