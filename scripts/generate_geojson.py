#!/usr/bin/env python3
"""
Generate geo/travel.geojson from logseq-content location pages.

Reads:  /home/rocky/logseq-content/pages/*.md  (read-only)
Writes: /home/rocky/projects/tools-obsidian/geo/travel.geojson

Coordinates are resolved from KNOWN_COORDS dict (pages have no GPS data).
Places without known coords get coordinates: null and are listed separately.
"""

import json
import re
import sys
from pathlib import Path

PAGES_DIR = Path("/home/rocky/logseq-content/pages")
GEO_DIR   = Path("/home/rocky/projects/tools-obsidian/geo")
OUTPUT    = GEO_DIR / "travel.geojson"

# Known coordinates [lon, lat] for cities and specific places
KNOWN_COORDS: dict[str, list[float]] = {
    # Australia
    "Брисбен": [153.0251, -27.4698],
    "Brisbane": [153.0251, -27.4698],
    "Голд Кост": [153.4217, -28.0167],
    "Gold Coast": [153.4217, -28.0167],
    "Мельбурн": [144.9631, -37.8136],
    "Melbourne": [144.9631, -37.8136],
    "Сидней": [151.2093, -33.8688],
    "Sydney": [151.2093, -33.8688],
    "Австралия": [133.7751, -25.2744],
    # Gold Coast specific places
    "ASMY": [153.3830, -28.0600],           # Currumbin area
    "2 Santabelle": [153.4300, -28.0800],   # Robina area
    "59 Larnock": [153.4200, -28.0900],
    "Clear Island Waters": [153.3989, -28.0452],
    "Coolangatta": [153.5400, -28.1667],
    "Robina": [153.3826, -28.0799],
    "Pacific Fair": [153.4150, -28.0340],   # Broadbeach mall
    # Bali / Indonesia
    "Бали": [115.1889, -8.4095],
    "Bali": [115.1889, -8.4095],
    "Денпасар": [115.2126, -8.6705],
    "Denpasar": [115.2126, -8.6705],
    "Убуд": [115.2624, -8.5069],
    "Ubud": [115.2624, -8.5069],
    "Adi House Moding": [115.2630, -8.5080],
    "Чангу": [115.1367, -8.6569],
    # India
    "Индия": [78.9629, 20.5937],
    "India": [78.9629, 20.5937],
    "Дели": [77.2090, 28.6139],
    "Delhi": [77.2090, 28.6139],
    "Вриндаван": [77.7027, 27.5795],
    "Vrindavan": [77.7027, 27.5795],
    "Матхура": [77.6737, 27.4924],
    # Nepal
    "Непал": [84.1240, 28.3949],
    "Nepal": [84.1240, 28.3949],
    "Катманду": [85.3240, 27.7172],
    "Kathmandu": [85.3240, 27.7172],
    # Kazakhstan
    "Казахстан": [66.9237, 48.0196],
    "Алматы": [76.8512, 43.2220],
    "Almaty": [76.8512, 43.2220],
    # Russia
    "Россия": [105.3188, 61.5240],
    "Москва": [37.6173, 55.7558],
    "Moscow": [37.6173, 55.7558],
    # Brazil
    "Бразилия": [-51.9253, -14.2350],
    # Guatemala
    "Гватемала": [-90.5069, 14.6349],
}

# Location type labels
TYPE_LABEL = {
    "страна": "country",
    "город": "city",
    "дом": "home",
    "ashram": "ashram",
    "ашрам": "ashram",
    "кафе": "cafe",
    "cafe": "cafe",
    "адрес": "address",
}

PROP_RE = re.compile(r"^-?\s*([A-Za-zА-Яа-яёЁ_-]+)::\s*(.+)$")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
PLACE_RE = re.compile(
    r"#место|Тип::\s*(Город|Страна|Дом|Кафе|Адрес|Ашрам)",
    re.IGNORECASE,
)


def parse_props(lines: list[str]) -> dict[str, str]:
    props: dict[str, str] = {}
    for line in lines:
        m = PROP_RE.match(line.strip())
        if m:
            props[m.group(1).lower().strip()] = m.group(2).strip()
    return props


def resolve_coords(name: str, location: str) -> list[float] | None:
    """Resolve coords: prefer most specific match (place > city > country)."""
    # Specificity: more chars in key = more specific (city > country)
    candidates: list[tuple[int, list[float]]] = []

    for text in [name, location]:
        if text in KNOWN_COORDS:
            candidates.append((len(text), KNOWN_COORDS[text]))
        for link in WIKILINK_RE.findall(text):
            if link in KNOWN_COORDS:
                candidates.append((len(link), KNOWN_COORDS[link]))

    if not candidates:
        return None
    # return coords of most specific match (longest key)
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def build_feature(path: Path) -> dict | None:
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception:
        return None

    if not PLACE_RE.search(raw):
        return None

    lines = raw.splitlines()
    props = parse_props(lines)

    place_type_raw = props.get("тип", props.get("type", "")).lower()
    place_type = TYPE_LABEL.get(place_type_raw, place_type_raw or "place")

    location_raw = props.get("локация", props.get("location", props.get("страна", "")))
    location_links = WIKILINK_RE.findall(location_raw)
    location = ", ".join(location_links) if location_links else location_raw

    description = props.get("описание", props.get("description", ""))
    description = re.sub(r"\[\[([^\]]+)\]\]", r"\1", description)

    alias = props.get("alias", "")

    name = path.stem
    coords = resolve_coords(name, location_raw)

    feature: dict = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": coords} if coords else None,
        "properties": {
            "name": name,
            "type": place_type,
        },
    }
    if location:
        feature["properties"]["location"] = location
    if description:
        feature["properties"]["description"] = description
    if alias:
        feature["properties"]["alias"] = alias

    return feature


def build_travel_route() -> list[dict]:
    """Build a LineString of known visited cities in chronological order."""
    # Known travel route based on journals and flight records
    route_points = [
        # Russia → Bali (initial move, pre-2020)
        {"name": "Москва", "coords": KNOWN_COORDS["Москва"]},
        # Bali period
        {"name": "Денпасар", "coords": KNOWN_COORDS["Денпасар"]},
        {"name": "Убуд", "coords": KNOWN_COORDS["Убуд"]},
        # India pilgrimages (2023)
        {"name": "Дели", "coords": KNOWN_COORDS["Дели"]},
        {"name": "Вриндаван", "coords": KNOWN_COORDS["Вриндаван"]},
        # Nepal (2023)
        {"name": "Катманду", "coords": KNOWN_COORDS["Катманду"]},
        # Australia (2023-present)
        {"name": "Брисбен", "coords": KNOWN_COORDS["Брисбен"]},
        {"name": "Мельбурн", "coords": KNOWN_COORDS["Мельбурн"]},
        {"name": "Голд Кост", "coords": KNOWN_COORDS["Голд Кост"]},
        # Back to Bali (2025-2026 period)
        {"name": "Убуд", "coords": KNOWN_COORDS["Убуд"]},
        # Return to Australia
        {"name": "Голд Кост", "coords": KNOWN_COORDS["Голд Кост"]},
    ]

    coordinates = [p["coords"] for p in route_points]
    return [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coordinates,
            },
            "properties": {
                "name": "Travel route",
                "type": "route",
                "description": "Approximate travel history (manually curated)",
            },
        }
    ]


def main():
    GEO_DIR.mkdir(parents=True, exist_ok=True)

    all_pages = sorted(PAGES_DIR.glob("*.md"))
    print(f"Scanning {len(all_pages)} pages for locations...", file=sys.stderr)

    features: list[dict] = []
    unknown_coords: list[str] = []

    for page in all_pages:
        f = build_feature(page)
        if f is None:
            continue
        if f["geometry"] is None:
            unknown_coords.append(f["properties"]["name"])
        features.append(f)

    # Add travel route
    features = build_travel_route() + features

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    OUTPUT.write_text(json.dumps(geojson, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Written {len(features)} features to {OUTPUT}", file=sys.stderr)
    print(f"  with coords: {len(features) - len(unknown_coords)}", file=sys.stderr)
    if unknown_coords:
        print(f"  coords unknown ({len(unknown_coords)}): {', '.join(unknown_coords[:10])}", file=sys.stderr)


if __name__ == "__main__":
    main()
