#!/usr/bin/env python3
"""
Logseq Expenses.md → beancount converter.

Source:  /home/rocky/logseq-content/pages/Expenses.md
Output:  /home/rocky/projects/tools-obsidian/finance/main.beancount

Format of source (Logseq outline, tabs as indent):
  - ## 2026
    - ### January
      - [[2026-01-01]]
        id:: <uuid>
        collapsed:: true
          - #category [#payee] Description
            currency:: amount
"""

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

SOURCE = Path("/home/rocky/logseq-content/pages/Expenses.md")
OUTPUT = Path("/home/rocky/projects/tools-obsidian/finance/main.beancount")

# ─── Category → beancount account ───────────────────────────────────────────

CATEGORY_MAP: dict[str, str] = {
    # Food & drink
    "food": "Expenses:Food",
    "foode": "Expenses:Food",
    "cafe": "Expenses:Food:Cafe",
    "delivery": "Expenses:Food:Delivery",
    "delivey": "Expenses:Food:Delivery",
    "take-away": "Expenses:Food",
    "milk": "Expenses:Food",
    "jamu": "Expenses:Food",
    "buffet": "Expenses:Food",
    # Shopping
    "shopping": "Expenses:Shopping",
    "shop": "Expenses:Shopping",
    "clothes": "Expenses:Clothing",
    "candle": "Expenses:Shopping",
    # Transport
    "taxi": "Expenses:Transport:Taxi",
    "transport": "Expenses:Transport",
    "bus": "Expenses:Transport",
    "flight": "Expenses:Transport:Flight",
    "plane": "Expenses:Transport:Flight",
    "car": "Expenses:Transport:Car",
    # Subscriptions & tech
    "subscription": "Expenses:Subscriptions",
    "subsription": "Expenses:Subscriptions",
    "app": "Expenses:Subscriptions:Apps",
    "apps": "Expenses:Subscriptions:Apps",
    "vps": "Expenses:Tech:Infrastructure",
    "infrastructure": "Expenses:Tech:Infrastructure",
    "Проекты": "Expenses:Tech:Projects",
    # Health
    "health": "Expenses:Health",
    "здоровье": "Expenses:Health",
    "massage": "Expenses:Health:Wellness",
    "spa": "Expenses:Health:Wellness",
    "coconut-spa": "Expenses:Health:Wellness",
    "dentist": "Expenses:Health:Dental",
    "pharmacy": "Expenses:Health:Pharmacy",
    "remedy": "Expenses:Health:Pharmacy",
    "vitamin": "Expenses:Health:Vitamins",
    "vaccine": "Expenses:Health:Medical",
    "therapy": "Expenses:Health:Therapy",
    # Personal care
    "barbershop": "Expenses:Grooming",
    "Barbershop": "Expenses:Grooming",
    "shaving": "Expenses:Grooming",
    "laundry": "Expenses:Laundry",
    # Housing
    "rent": "Expenses:Housing:Rent",
    "housing": "Expenses:Housing",
    "house": "Expenses:Housing",
    "accomodation": "Expenses:Accommodation",
    # Travel
    "travel": "Expenses:Travel",
    "camping": "Expenses:Travel:Camping",
    # Education
    "education": "Expenses:Education",
    "book": "Expenses:Education:Books",
    "english": "Expenses:Education:Language",
    # Entertainment
    "IMAX": "Expenses:Entertainment:Cinema",
    "music": "Expenses:Entertainment:Music",
    "guitar": "Expenses:Entertainment:Music",
    # Telecom
    "mobile": "Expenses:Telecom:Mobile",
    "telecom": "Expenses:Telecom",
    "sim": "Expenses:Telecom:SIM",
    "mobile-internet": "Expenses:Telecom:Internet",
    "Mobile-Internet": "Expenses:Telecom:Internet",
    # Gifts & culture
    "flowers": "Expenses:Gifts:Flowers",
    "flower-shop": "Expenses:Gifts:Flowers",
    "donation": "Expenses:Donations",
    "ceremony": "Expenses:Culture:Ceremony",
    # Services & admin
    "service": "Expenses:Services",
    "servise": "Expenses:Services",
    "fix": "Expenses:Services:Repair",
    "hardware": "Expenses:Services:Repair",
    "print": "Expenses:Services:Print",
    "printing": "Expenses:Services:Print",
    "docs": "Expenses:Services:Documents",
    "kitas": "Expenses:Services:Documents",
    "consulting": "Expenses:Services",
    "fee": "Expenses:Fees",
    "transactions": "Expenses:Fees",
    "taxkz": "Expenses:Fees:Tax",
    # Financial
    "income": "Income:Other",
    "CRM": "Income:CRM",
    "CMR": "Income:CRM",
    "debt": "Liabilities:Debt",
    "atm": "Assets:Cash",
    "ATM": "Assets:Cash",
    "cash": "Assets:Cash",
    "Cash": "Assets:Cash",
    # Misc
    "other": "Expenses:Other",
    "direct": "Expenses:Other",
    "signature": "Expenses:Other",
    "etke": "Expenses:Other",
    "sox": "Expenses:Other",
    "cow": "Expenses:Other",
}

MONTH_MAP = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}

CURRENCY_RE = re.compile(r"^(aud|idr|usd|rub|kzt)::\s*([\d.,]+)", re.IGNORECASE)
DATE_RE = re.compile(r"\[\[(\d{4}-\d{2}-\d{2})\]\]")
TAG_RE = re.compile(r"#\[\[([^\]]+)\]\]|#([A-Za-zА-Яа-я0-9_:-]+)")
YEAR_RE = re.compile(r"^##\s+(\d{4})\s*$")
MONTH_RE = re.compile(r"^###\s+(\w+)\s*$")


@dataclass
class Item:
    date: str
    tags: list[str]
    description: str
    currencies: dict[str, float] = field(default_factory=dict)


def count_tabs(line: str) -> int:
    n = 0
    for ch in line:
        if ch == "\t":
            n += 1
        else:
            break
    return n


def strip_bullet(text: str) -> str:
    """Remove leading '- ' from a bullet line (after tabs)."""
    t = text.lstrip("\t")
    if t.startswith("- "):
        return t[2:]
    return t


def parse_tags(text: str) -> tuple[list[str], str]:
    """
    Extract #tags from text.
    Returns (tags_list, remaining_description).
    """
    tags = []
    pos = 0
    result_parts = []
    for m in TAG_RE.finditer(text):
        # text between previous match and this one
        between = text[pos:m.start()]
        if between.strip():
            result_parts.append(between)
        tag = m.group(1) or m.group(2)  # [[Tag]] or simple
        tags.append(tag)
        pos = m.end()
    tail = text[pos:]
    if tail.strip():
        result_parts.append(tail)
    description = "".join(result_parts).strip().strip(",").strip()
    return tags, description


def resolve_account(tags: list[str]) -> tuple[str, Optional[str], list[str]]:
    """
    Returns (account, payee, remaining_tags).
    First recognized category tag → account.
    Non-category tags → payee (joined if multiple).
    """
    account = "Expenses:Other"
    payee_parts: list[str] = []
    remaining: list[str] = []
    account_found = False

    for tag in tags:
        key = tag.lower()
        # Try exact match first, then lowercase
        if not account_found and tag in CATEGORY_MAP:
            account = CATEGORY_MAP[tag]
            account_found = True
        elif not account_found and key in CATEGORY_MAP:
            account = CATEGORY_MAP[key]
            account_found = True
        else:
            payee_parts.append(tag.replace("-", " ").replace("_", " "))

    payee = " / ".join(payee_parts) if payee_parts else None
    return account, payee, remaining


def format_amount(amount: float) -> str:
    """Format number: drop .0 if integer, else keep up to 2 decimal places."""
    if amount == int(amount):
        return str(int(amount))
    return f"{amount:.2f}"


def item_to_beancount(item: Item) -> str:
    """Convert an Item to a beancount transaction string."""
    tags, description = parse_tags(" ".join(
        f"#[[{t}]]" if " " in t else f"#{t}" for t in item.tags
    ) + " " + item.description)
    # Re-parse from the original item
    tags = item.tags
    description = item.description

    account, payee, _ = resolve_account(tags)
    narration = description or (tags[0] if tags else "")
    payee_str = f'"{payee}" ' if payee else ""

    currencies = item.currencies
    lines = [f'{item.date} * {payee_str}"{narration}"']

    if not currencies:
        lines.append(f"  {account}  0 AUD")
        lines.append(f"  Assets:Cash  0 AUD")
        return "\n".join(lines)

    # Income/liability accounts: flip sign so Assets:Cash is debited (positive)
    is_income = account.startswith("Income:") or account.startswith("Liabilities:")

    # Determine posting structure
    if "aud" in currencies and len(currencies) == 1:
        amt = format_amount(currencies["aud"])
        if is_income:
            lines.append(f"  Assets:Cash  {amt} AUD")
            lines.append(f"  {account}  -{amt} AUD")
        else:
            lines.append(f"  {account}  {amt} AUD")
            lines.append(f"  Assets:Cash  -{amt} AUD")

    elif len(currencies) == 1:
        # Single non-AUD currency
        ccy, amt_raw = next(iter(currencies.items()))
        amt = format_amount(amt_raw)
        lines.append(f"  {account}  {amt} {ccy.upper()}")
        lines.append(f"  Assets:Cash  -{amt} {ccy.upper()}")

    elif "aud" in currencies and len(currencies) == 2:
        # Foreign + AUD: record in AUD (converted), preserve original in comment
        foreign_ccy = next(c for c in currencies if c != "aud")
        foreign_amt = currencies[foreign_ccy]
        aud_amt = currencies["aud"]
        f_amt = format_amount(foreign_amt)
        a_amt = format_amount(aud_amt)
        lines.append(f"  {account}  {a_amt} AUD ; {f_amt} {foreign_ccy.upper()}")
        lines.append(f"  Assets:Cash  -{a_amt} AUD")

    else:
        # Multiple foreign currencies or 3+ currencies — one posting per currency
        for ccy, amt_raw in currencies.items():
            amt = format_amount(amt_raw)
            lines.append(f"  {account}  {amt} {ccy.upper()}")
            lines.append(f"  Assets:Cash  -{amt} {ccy.upper()}")

    return "\n".join(lines)


def parse_expenses_md(path: Path) -> list[Item]:
    """Parse Logseq outline Expenses.md and return list of Items."""
    items: list[Item] = []
    current_year: Optional[int] = None
    current_month: Optional[int] = None
    current_date: Optional[str] = None
    current_item: Optional[Item] = None
    in_query = False

    lines = path.read_text(encoding="utf-8").splitlines()

    for raw in lines:
        line = raw.rstrip("\r")
        tabs = count_tabs(line)
        content = line.lstrip("\t")

        # Skip Logseq queries
        if "#+BEGIN_QUERY" in content:
            in_query = True
            continue
        if "#+END_QUERY" in content:
            in_query = False
            continue
        if in_query:
            continue

        # Property lines (no leading "- ")
        if not content.startswith("- "):
            m = CURRENCY_RE.match(content.strip())
            if m and current_item is not None:
                ccy = m.group(1).lower()
                amt_str = m.group(2).replace(",", ".")
                current_item.currencies[ccy] = float(amt_str)
            # id::, collapsed::, etc. → skip
            continue

        # Bullet line
        text = content[2:].strip()  # strip "- "

        # Year header: "## 2026"
        m = YEAR_RE.match(text)
        if m:
            if current_item is not None:
                items.append(current_item)
                current_item = None
            current_year = int(m.group(1))
            current_month = None
            current_date = None
            continue

        # Month header: "### January"
        m = MONTH_RE.match(text)
        if m and m.group(1) in MONTH_MAP:
            if current_item is not None:
                items.append(current_item)
                current_item = None
            current_month = MONTH_MAP[m.group(1)]
            current_date = None
            continue

        # Date block: "[[YYYY-MM-DD]]"
        m = DATE_RE.match(text)
        if m:
            if current_item is not None:
                items.append(current_item)
                current_item = None
            current_date = m.group(1)
            continue

        # Item line (under a date block): starts with #tag or plain text
        if current_date and not text.startswith("#+"):
            # Save previous item
            if current_item is not None:
                items.append(current_item)
            tags, description = parse_tags(text)
            current_item = Item(
                date=current_date,
                tags=tags,
                description=description,
            )
            continue

    # Flush last item
    if current_item is not None:
        items.append(current_item)

    return items


def collect_accounts(items: list[Item]) -> set[str]:
    accounts = {"Assets:Cash"}
    for item in items:
        account, _, _ = resolve_account(item.tags)
        accounts.add(account)
    return accounts


def build_beancount(items: list[Item]) -> str:
    if not items:
        return ""

    accounts = collect_accounts(items)
    currencies_used: set[str] = {"AUD"}
    for item in items:
        currencies_used.update(c.upper() for c in item.currencies)

    start_date = min(item.date for item in items)

    parts: list[str] = []

    # Header
    parts.append('; Generated by expenses_to_beancount.py')
    parts.append('; Source: /home/rocky/logseq-content/pages/Expenses.md')
    parts.append('')
    parts.append('option "operating_currency" "AUD"')
    parts.append('option "title" "Personal Finance"')
    parts.append('')

    # Commodity declarations
    for ccy in sorted(currencies_used):
        parts.append(f'{start_date} commodity {ccy}')
    parts.append('')

    # Account opens
    for acc in sorted(accounts):
        parts.append(f'{start_date} open {acc}')
    parts.append('')

    # Transactions
    for item in items:
        parts.append(item_to_beancount(item))
        parts.append('')

    return "\n".join(parts)


def main():
    if not SOURCE.exists():
        print(f"ERROR: source not found: {SOURCE}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {SOURCE}...", file=sys.stderr)
    items = parse_expenses_md(SOURCE)
    print(f"  parsed {len(items)} items", file=sys.stderr)

    beancount = build_beancount(items)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(beancount, encoding="utf-8")
    print(f"Written: {OUTPUT}", file=sys.stderr)
    print(f"  transactions: {len(items)}", file=sys.stderr)

    # Quick stats
    from collections import Counter
    acct_counts: Counter = Counter()
    for item in items:
        acct, _, _ = resolve_account(item.tags)
        acct_counts[acct] += 1
    print("\nTop accounts:", file=sys.stderr)
    for acct, cnt in acct_counts.most_common(10):
        print(f"  {cnt:4d}  {acct}", file=sys.stderr)


if __name__ == "__main__":
    main()
