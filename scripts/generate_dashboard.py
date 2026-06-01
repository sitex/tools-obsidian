#!/usr/bin/env python3
"""Generate finance/dashboard.md from beancount ledger."""

import argparse
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

try:
    from beancount import loader
    from beancount.core import data, amount
    from beancount.core.number import Decimal
except ImportError:
    sys.exit("beancount not installed: pip install beancount")


def load_ledger(path: str):
    entries, errors, options = loader.load_file(path)
    if errors:
        for e in errors:
            print(f"WARNING: {e}", file=sys.stderr)
    return entries, options


def get_aud(posting) -> Decimal | None:
    """Return AUD amount from posting, or None if not AUD."""
    if posting.units.currency == "AUD":
        return posting.units.number
    return None


def build_monthly_by_category(entries) -> dict:
    """Returns {(year, month): {account: Decimal(AUD)}}"""
    result = defaultdict(lambda: defaultdict(Decimal))
    for entry in entries:
        if not isinstance(entry, data.Transaction):
            continue
        y, m = entry.date.year, entry.date.month
        for posting in entry.postings:
            if not posting.account.startswith("Expenses:"):
                continue
            aud = get_aud(posting)
            if aud is not None:
                result[(y, m)][posting.account] += aud
    return result


def build_monthly_totals(monthly: dict) -> dict:
    """Returns {(year, month): Decimal(AUD total)}"""
    return {ym: sum(v.values()) for ym, v in monthly.items()}


def top_categories(monthly_data: dict, n: int = 10) -> list:
    """Return top N (account, total) sorted by total desc."""
    totals = defaultdict(Decimal)
    for cats in monthly_data.values():
        for acc, amt in cats.items():
            totals[acc] += amt
    return sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]


def shorten_account(account: str) -> str:
    return account.replace("Expenses:", "")


def format_aud(n: Decimal) -> str:
    return f"A${n:,.2f}"


def generate_markdown(entries, options, ledger_path: str, months_back: int = 12) -> str:
    monthly = build_monthly_by_category(entries)
    totals = build_monthly_totals(monthly)

    today = date.today()
    cur_ym = (today.year, today.month)

    # Last N months sorted
    all_months = sorted(totals.keys())
    recent_months = [ym for ym in all_months if (
        ym[0] * 12 + ym[1] >= (today.year - months_back // 12) * 12 + today.month - months_back
    )][-months_back:]

    lines = [
        f"# Финансовый дашборд",
        f"",
        f"> Сгенерировано: {datetime.now().strftime('%Y-%m-%d %H:%M')}  ",
        f"> Источник: `{ledger_path}`  ",
        f"> Транзакций всего: {sum(1 for e in entries if isinstance(e, data.Transaction))}",
        f"",
    ]

    # --- Current month ---
    cur_data = monthly.get(cur_ym, {})
    cur_total = totals.get(cur_ym, Decimal(0))
    lines += [
        f"## Текущий месяц ({today.strftime('%B %Y')})",
        f"",
        f"**Итого:** {format_aud(cur_total)}",
        f"",
        f"| Категория | Сумма |",
        f"|-----------|-------|",
    ]
    for acc, amt in sorted(cur_data.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"| {shorten_account(acc)} | {format_aud(amt)} |")

    lines.append("")

    # --- Monthly trend ---
    lines += [
        f"## Тренд по месяцам (последние {len(recent_months)} мес.)",
        f"",
        f"| Месяц | Расходы AUD |",
        f"|-------|-------------|",
    ]
    for ym in recent_months:
        label = date(ym[0], ym[1], 1).strftime("%Y-%m")
        marker = " ← текущий" if ym == cur_ym else ""
        lines.append(f"| {label} | {format_aud(totals[ym])}{marker} |")

    if recent_months:
        avg = sum(totals[ym] for ym in recent_months) / len(recent_months)
        lines += ["", f"**Среднее/мес:** {format_aud(avg)}", ""]

    # --- Top categories all time ---
    lines += [
        "## Топ категорий (за всё время)",
        "",
        "| Категория | Итого AUD |",
        "|-----------|-----------|",
    ]
    for acc, amt in top_categories(monthly):
        lines.append(f"| {shorten_account(acc)} | {format_aud(amt)} |")

    lines.append("")

    # --- Multi-currency summary ---
    currency_totals: dict[str, Decimal] = defaultdict(Decimal)
    for entry in entries:
        if not isinstance(entry, data.Transaction):
            continue
        for posting in entry.postings:
            if posting.account.startswith("Expenses:"):
                currency_totals[posting.units.currency] += posting.units.number

    non_aud = {c: v for c, v in currency_totals.items() if c != "AUD"}
    if non_aud:
        lines += [
            "## Мультивалютные расходы (оригинальные суммы)",
            "",
            "| Валюта | Сумма |",
            "|--------|-------|",
        ]
        lines.append(f"| AUD | {format_aud(currency_totals['AUD'])} |")
        for cur, amt in sorted(non_aud.items()):
            lines.append(f"| {cur} | {amt:,.0f} |")
        lines.append("")

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate finance dashboard from beancount")
    parser.add_argument("--ledger", default="finance/main.beancount",
                        help="Path to beancount file")
    parser.add_argument("--output", default="finance/dashboard.md",
                        help="Output markdown file")
    parser.add_argument("--months", type=int, default=12,
                        help="Months of trend to show")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print to stdout instead of writing file")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    ledger_path = repo_root / args.ledger
    output_path = repo_root / args.output

    if not ledger_path.exists():
        sys.exit(f"Ledger not found: {ledger_path}")

    entries, options = load_ledger(str(ledger_path))
    md = generate_markdown(entries, options, str(ledger_path), months_back=args.months)

    if args.dry_run:
        print(md)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md, encoding="utf-8")
        print(f"Dashboard written: {output_path}")


if __name__ == "__main__":
    main()
