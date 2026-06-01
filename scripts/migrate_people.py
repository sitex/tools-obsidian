#!/usr/bin/env python3
"""
Migrate person pages from logseq-content/pages/ → tools-obsidian/people/

Reads:  /home/rocky/logseq-content/pages/*.md  (read-only)
Writes: /home/rocky/projects/tools-obsidian/people/*.md

Detection: pages with #человек, Тип:: Человек, or type:: [[Person]]
Output:   YAML frontmatter + cleaned Logseq content
"""

import re
import sys
from pathlib import Path

PAGES_DIR  = Path("/home/rocky/logseq-content/pages")
PEOPLE_DIR = Path("/home/rocky/projects/tools-obsidian/people")

PERSON_MARKERS = [
    r"#человек",
    r"Тип::\s*Человек",
    r"type::\s*\[\[Person\]\]",
]
PERSON_RE = re.compile("|".join(PERSON_MARKERS), re.IGNORECASE)

# ─── Property extractors ─────────────────────────────────────────────────────

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
TAG_RE      = re.compile(r"#([A-Za-zА-Яа-яёЁ0-9_-]+)")
PROP_RE     = re.compile(r"^-?\s*([A-Za-zА-Яа-яёЁ_-]+)::\s*(.+)$")
DATE_RE     = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def extract_wikilinks(text: str) -> list[str]:
    return WIKILINK_RE.findall(text)


def parse_logseq_props(lines: list[str]) -> dict[str, str]:
    """Extract key:: value properties from Logseq outline."""
    props: dict[str, str] = {}
    for line in lines:
        m = PROP_RE.match(line.strip())
        if m:
            k = m.group(1).lower().strip()
            v = m.group(2).strip()
            props[k] = v
    return props


def extract_location(props: dict, raw_text: str) -> str:
    """Resolve location from properties."""
    for key in ("location", "локация", "location::"):
        if key in props:
            links = extract_wikilinks(props[key])
            return ", ".join(links) if links else props[key]
    return ""


def extract_tags(lines: list[str]) -> list[str]:
    tags: set[str] = set()
    for line in lines:
        # tags:: line
        if re.match(r"^-?\s*tags::", line.strip(), re.IGNORECASE):
            found = TAG_RE.findall(line)
            tags.update(t.lower() for t in found if t.lower() not in ("человек",))
        # standalone #tag (only top-level / property lines)
        elif line.strip().startswith("-") and "#" in line:
            found = TAG_RE.findall(line[:80])
            for t in found:
                if t.lower() not in ("человек", "контакт"):
                    tags.add(t.lower())
    return sorted(tags)


def extract_last_date(raw_text: str) -> str:
    dates = DATE_RE.findall(raw_text)
    return max(dates) if dates else ""


def clean_content(lines: list[str]) -> str:
    """Remove Logseq-specific metadata, keep human-readable content."""
    skip_patterns = [
        r"^-?\s*[A-Za-zА-Яа-яёЁ_-]+::\s*",  # any key:: value property
        r"^-?\s*#человек\s*$",
        r"^-?\s*---\s*$",
    ]
    skip_re = re.compile("|".join(skip_patterns), re.IGNORECASE)

    result: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if skip_re.match(stripped):
            continue
        # Convert "- ## Heading" → "## Heading"
        heading = re.match(r"^-\s+(#{1,3}\s+.+)$", stripped)
        if heading:
            result.append(heading.group(1))
            continue
        # Convert "- text" → "text" (top-level bullets)
        bullet = re.match(r"^-\s+(.+)$", stripped)
        if bullet:
            result.append(bullet.group(1))
            continue
        result.append(stripped)

    return "\n".join(result).strip()


def is_person_page(text: str) -> bool:
    return bool(PERSON_RE.search(text))


def process_page(path: Path) -> tuple[str, str] | None:
    """
    Returns (filename, md_content) or None if not a person page.
    """
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception:
        return None

    if not is_person_page(raw):
        return None

    lines = raw.splitlines()
    props = parse_logseq_props(lines)
    location = extract_location(props, raw)
    tags = extract_tags(lines)
    last_date = extract_last_date(raw)
    name = path.stem  # filename without .md

    # Extra human-useful properties
    description = props.get("описание", props.get("description", ""))
    # Extract wikilinks from any relationship-style props
    rel_props = {k: v for k, v in props.items()
                 if k not in ("type", "тип", "location", "локация", "страна",
                               "tags", "collapsed", "id", "описание", "description")}

    # Build frontmatter
    fm_lines = ["---", f"name: {name}"]
    if location:
        fm_lines.append(f"location: {location}")
    if description:
        desc_clean = re.sub(r"\[\[([^\]]+)\]\]", r"\1", description)
        fm_lines.append(f"description: {desc_clean}")
    if tags:
        tag_str = ", ".join(tags)
        fm_lines.append(f"tags: [{tag_str}]")
    if last_date:
        fm_lines.append(f"last_contact: {last_date}")
    # Relationship props (жена::, муж:: etc.)
    for k, v in rel_props.items():
        links = extract_wikilinks(v)
        val = ", ".join(links) if links else v
        fm_lines.append(f"{k}: {val}")
    fm_lines.append(f"source: logseq:pages/{path.name}")
    fm_lines.append("---")

    body = clean_content(lines)
    md = "\n".join(fm_lines)
    if body:
        md += "\n\n" + body

    # Sanitize filename: keep alphanumeric, spaces→dash, strip unsafe
    safe_name = re.sub(r"[^\w\s-]", "", name)
    safe_name = re.sub(r"\s+", "-", safe_name.strip())
    filename = safe_name + ".md"

    return filename, md


def main():
    PEOPLE_DIR.mkdir(parents=True, exist_ok=True)

    all_pages = sorted(PAGES_DIR.glob("*.md"))
    print(f"Scanning {len(all_pages)} pages...", file=sys.stderr)

    written = skipped = 0
    for page in all_pages:
        result = process_page(page)
        if result is None:
            skipped += 1
            continue
        filename, content = result
        out = PEOPLE_DIR / filename
        out.write_text(content, encoding="utf-8")
        written += 1

    print(f"Done: {written} people files written to {PEOPLE_DIR}", file=sys.stderr)
    print(f"Skipped (not person pages): {skipped}", file=sys.stderr)


if __name__ == "__main__":
    main()
