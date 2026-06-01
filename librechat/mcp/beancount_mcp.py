#!/usr/bin/env python3
"""
Beancount MCP Server — stdio JSON-RPC 2.0 transport.
Монтирует /data/main.beancount (read-only).

Tools:
  query_expenses        — агрегаты расходов за год/месяц/категорию
  get_monthly_totals    — помесячные итоги за последние N месяцев
"""

import sys
import json
import decimal
from datetime import date, timedelta
from collections import defaultdict
from typing import Any

# beancount 3.x imports
from beancount import loader
from beancount.core import data, amount, convert
from beancount.core.number import D

BEANCOUNT_FILE = "/data/main.beancount"

# ---------------------------------------------------------------------------
# Beancount helpers
# ---------------------------------------------------------------------------

def load_entries():
    entries, errors, options = loader.load_file(BEANCOUNT_FILE)
    return entries, options


def _txn_date(entry) -> date:
    return entry.date


def _account_category(account: str) -> str:
    """Верхний уровень счёта после 'Expenses:', напр. 'Food'."""
    parts = account.split(":")
    if len(parts) >= 2:
        return parts[1]
    return parts[0]


def query_expenses(year: int, month: int | None = None, category: str | None = None) -> dict:
    """
    Возвращает агрегаты расходов.
    Группировка: category -> currency -> total
    """
    entries, options = load_entries()
    home_currency = options.get("operating_currency", ["USD"])[0]

    totals: dict[str, dict[str, decimal.Decimal]] = defaultdict(lambda: defaultdict(decimal.Decimal))

    for entry in entries:
        if not isinstance(entry, data.Transaction):
            continue

        txn_date = _txn_date(entry)
        if txn_date.year != year:
            continue
        if month is not None and txn_date.month != month:
            continue

        for posting in entry.postings:
            if not posting.account.startswith("Expenses:"):
                continue

            cat = _account_category(posting.account)
            if category is not None and cat.lower() != category.lower():
                continue

            units = posting.units
            if units is None:
                continue

            totals[cat][units.currency] += units.number

    # Сериализуем Decimal → str
    result = {}
    for cat, currencies in totals.items():
        result[cat] = {cur: str(amt) for cur, amt in currencies.items()}

    period_label = f"{year}-{month:02d}" if month else str(year)
    return {
        "period": period_label,
        "category_filter": category,
        "totals": result,
        "num_categories": len(result),
    }


def get_monthly_totals(n_months: int = 12) -> dict:
    """
    Возвращает помесячные итоги расходов за последние n_months месяцев.
    """
    entries, options = load_entries()
    today = date.today()

    # Вычисляем список (year, month) за последние n_months
    months = []
    y, m = today.year, today.month
    for _ in range(n_months):
        months.append((y, m))
        m -= 1
        if m == 0:
            m = 12
            y -= 1
    months.reverse()

    # Агрегация: (year, month) -> currency -> Decimal
    totals: dict[tuple, dict[str, decimal.Decimal]] = {
        (y, m): defaultdict(decimal.Decimal) for y, m in months
    }

    for entry in entries:
        if not isinstance(entry, data.Transaction):
            continue

        key = (_txn_date(entry).year, _txn_date(entry).month)
        if key not in totals:
            continue

        for posting in entry.postings:
            if not posting.account.startswith("Expenses:"):
                continue
            units = posting.units
            if units is None:
                continue
            totals[key][units.currency] += units.number

    result = []
    for (y, m) in months:
        currencies = totals[(y, m)]
        result.append({
            "month": f"{y}-{m:02d}",
            "totals": {cur: str(amt) for cur, amt in currencies.items()},
        })

    return {
        "n_months": n_months,
        "monthly_totals": result,
    }


# ---------------------------------------------------------------------------
# MCP JSON-RPC 2.0 stdio transport
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "query_expenses",
        "description": (
            "Возвращает агрегированные расходы из beancount за указанный период. "
            "Группировка по категории (второй уровень счёта Expenses:)."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "year": {
                    "type": "integer",
                    "description": "Год (обязательный), например 2025",
                },
                "month": {
                    "type": "integer",
                    "description": "Месяц 1–12 (опциональный). Если не указан — весь год.",
                    "minimum": 1,
                    "maximum": 12,
                },
                "category": {
                    "type": "string",
                    "description": "Фильтр по категории расходов, напр. 'Food' или 'Transport' (опциональный).",
                },
            },
            "required": ["year"],
        },
    },
    {
        "name": "get_monthly_totals",
        "description": (
            "Возвращает помесячные итоги расходов за последние N месяцев. "
            "Удобно для обзора трат за квартал/полугодие/год."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "n_months": {
                    "type": "integer",
                    "description": "Количество последних месяцев (по умолчанию 12).",
                    "minimum": 1,
                    "maximum": 60,
                    "default": 12,
                },
            },
            "required": [],
        },
    },
]


def send(obj: Any) -> None:
    line = json.dumps(obj, ensure_ascii=False)
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def error_response(req_id: Any, code: int, message: str) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": code, "message": message},
    }


def handle_request(req: dict) -> dict | None:
    req_id = req.get("id")
    method = req.get("method", "")
    params = req.get("params", {})

    # Notifications (no id) — silently ignore
    if req_id is None and method != "notifications/initialized":
        return None

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "beancount-mcp",
                    "version": "1.0.0",
                },
            },
        }

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"tools": TOOLS},
        }

    if method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})

        try:
            if tool_name == "query_expenses":
                year = int(arguments["year"])
                month = int(arguments["month"]) if "month" in arguments else None
                category = arguments.get("category")
                result = query_expenses(year, month, category)

            elif tool_name == "get_monthly_totals":
                n_months = int(arguments.get("n_months", 12))
                result = get_monthly_totals(n_months)

            else:
                return error_response(req_id, -32601, f"Unknown tool: {tool_name}")

            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2),
                        }
                    ]
                },
            }

        except KeyError as e:
            return error_response(req_id, -32602, f"Missing required argument: {e}")
        except Exception as e:
            return error_response(req_id, -32603, f"Internal error: {e}")

    if method == "notifications/initialized":
        return None  # notification, no response

    return error_response(req_id, -32601, f"Method not found: {method}")


def main():
    for raw_line in sys.stdin:
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        try:
            req = json.loads(raw_line)
        except json.JSONDecodeError as e:
            send({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": f"Parse error: {e}"}})
            continue

        response = handle_request(req)
        if response is not None:
            send(response)


if __name__ == "__main__":
    main()
