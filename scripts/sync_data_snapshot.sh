#!/usr/bin/env bash
# Refresh tools-obsidian/data/pages/ from live logseq-content.
# Run when Expenses.md or people/location pages change in logseq-content.

set -euo pipefail

LOGSEQ="${LOGSEQ_CONTENT:-/home/rocky/logseq-content/pages}"
DATA="$(dirname "$0")/../data/pages"

echo "Syncing from $LOGSEQ → $DATA"

# Expenses
cp "$LOGSEQ/Expenses.md" "$DATA/Expenses.md"
echo "  Expenses.md"

# Person pages
count=0
while IFS= read -r -d '' f; do
    cp "$f" "$DATA/$(basename "$f")"
    ((count++))
done < <(grep -rlZ "#человек" "$LOGSEQ/")
echo "  $count person pages"

# Location pages
count=0
while IFS= read -r -d '' f; do
    cp "$f" "$DATA/$(basename "$f")"
    ((count++))
done < <(grep -rlZ "#место\|Тип:: Город\|Тип:: Страна\|Тип:: Регион" "$LOGSEQ/")
echo "  $count location pages"

echo "Done. Run 'git add data/ && git commit -m \"data: refresh snapshot\"' to commit."
