---
date: 2026-06-01T21:01:14+10:00
researcher: Ivan
git_commit: b6b6e5e1d
branch: main
repository: logseq-content
topic: "Logseq → Obsidian + beancount + LibreChat migration"
tags: [migration, obsidian, beancount, logseq, librechat, mcp]
status: in_progress
last_updated: 2026-06-01
last_updated_by: Claude
type: implementation_strategy
---

# Handoff: Миграция Logseq → гибридная архитектура

## Task(s)

Проектирование и поэтапная реализация перехода с Logseq на гибридную систему:
- **git-репо** как единственный источник истины (plain Markdown)
- **Obsidian** — десктоп/мобайл редактор
- **LibreChat + MCP** — чат-аналитика (data-over-views: ИИ не считает, а вызывает детерминированные движки)
- **beancount + Fava** — финансы
- **Dawarich** — гео-трекинг
- **Telegram-бот** — захват (уже работает, не трогать)

### Статус вех

| Веха | Статус | Описание |
|------|--------|----------|
| 0 — Гигиена | ✅ Частично | IP починен, webhook восстановлен, инвентарь block-refs создан. AI-чаты были перемещены → откачены (Logseq не трогать!) |
| 1 — Obsidian | 🔲 Не начато | Конфиг создавался, но откачен. Делать в tools-obsidian |
| 2 — beancount | 🔲 Не начато | Следующая приоритетная задача |
| 3 — Гео | 🔲 Не начато | |
| 4 — Голос/курсы | 🔲 Не начато | |
| 5 — Люди/проекты | 🔲 Не начато | |
| 6 — LibreChat+MCP | 🔲 Не начато | |

## Critical References

- **План:** `/home/rocky/.claude/plans/logseq-indexed-engelbart.md` — полный системный дизайн всех 7 вех
- **Финансы источник:** `/home/rocky/logseq-content/pages/Expenses.md` (4691 строк, май 2025 — июнь 2026)
- **Рабочий проект:** `/home/rocky/projects/tools-obsidian/` — сюда кладём ВСЕ инструменты и выходные файлы, НЕ в logseq-content

## Recent changes

Всё, что было сделано с `logseq-content`, ОТКАЧЕНО за исключением двух изменений:

1. `/home/rocky/logseq-content/scripts/webhook-server.py` — восстановлен сломанный сервис (файл был в `_delme_`, но сервис на него ссылался)
2. `/home/rocky/logseq-content/.gitignore` — добавлены строки `.obsidian/workspace*.json` и медиа расширения (безвредно)

Вне git (системные):
3. `/etc/logseq-automation.env` — VPS_IP исправлен: `161.97.81.151` → `217.216.76.5`
4. `~/.config/systemd/user/webhook-server.service` — отключён (дублировал системный процесс на порту 8080)

## Learnings

### Архитектура системы
- **Боты живут в** `/home/rocky/projects/logseq-services/` (монорепо): telegram-logger, logseq-helper, photo-bot, gps-bot
- **Деплой:** `deploy.sh` (rsync) → на Sydney `217.216.76.5`, user `claude`, path `/home/claude/logseq-services/`
- **Сервисы на Sydney:** `systemd` units под пользователем `claude`
- **Синк репо:** локальный `git-sync-debounce` (inotify → push после 30с тишины) + серверный pull через SSH триггер из `git-push-notify.sh`
- **Webhook:** `python3 /usr/local/bin/webhook-server.py` (PID управляется systemd, порт 8080) принимает POST от Sydney → `git-pull-notify.sh` (pull с rebase)

### Формат Expenses.md (для парсера beancount)
```
- ## 2026                    ← год (outline block, не markdown)
  - ### January              ← месяц  
    - [[2026-01-13]]         ← дата-блок
      id:: 723aab74-...      ← uuid для block-refs
      collapsed:: true
      - #category Описание #[[Payee]]   ← item строка
        aud:: 12             ← проперти суммы (следующая строка)
        idr:: 52000          ← мультивалюта: IDR = оригинал, AUD = конвертация
```

Валюты: `aud::` (812), `idr::` (580), `rub::` (35), `usd::` (9), `kzt::` (9)

**Грязь в данных:**
- `#subsription` (17 опечаток) вместо `#subscription`
- `#health` и `#здоровье` — дубли
- `#Coles`, `#GYG`, `#amazon` — это payee, не категории (первый `#тег` не всегда категория)
- Нет счёта-источника (карта/наличные) — задавать `Assets:Cash` по умолчанию
- Мультивалюта: один блок может содержать `idr::` + `usd::` + `aud::` одновременно

### Block-refs (381 активных)
- **266** — журналы → `logseq/bak/pages/Expenses/...` (старая bak-копия Expenses с теми же uuid). В Obsidian станут broken. При переходе на beancount эти ссылки теряют смысл — заменить на `[[Expenses]]` или удалить.
- **102** — cross-journal refs (между журналами)
- **13** — inter-page refs
- Полная карта: `/tmp/block-refs-inventory.csv` (локальный файл, не в git)

### Принципы (не нарушать)
- **logseq-content трогать минимально** — боты пишут туда, Logseq читает. Нет изменений формата.
- **ИИ оркеструет, детерминированные движки считают** — beancount, не LLM для сумм
- **Аудио в git НЕ класть** — только ссылки/пути

## Artifacts

- `/home/rocky/.claude/plans/logseq-indexed-engelbart.md` — **главный план**, читать перед началом любой вехи
- `/home/rocky/projects/tools-obsidian/` — рабочий проект для инструментов
- `/home/rocky/projects/logseq-services/` — монорепо ботов (telegram-logger, logseq-helper, photo-bot, gps-bot)

## Action Items & Next Steps

### Немедленно (Веха 2 — beancount парсер)
Создать `/home/rocky/projects/tools-obsidian/scripts/expenses_to_beancount.py`:

1. **Парсер outline** (идти по отступам, не по markdown-заголовкам):
   - Год: `- ## 2026` внутри outline block
   - Месяц: `- ### January`
   - Дата: `- [[YYYY-MM-DD]]` с опциональным `id::` на следующей строке
   - Item: `- #tag Описание [#payee]` + строка `currency:: amount`

2. **Маппинг тегов → beancount accounts:**
   - `#food` → `Expenses:Food`
   - `#shopping` → `Expenses:Shopping`
   - `#taxi` → `Expenses:Transport:Taxi`
   - `#subscription`/`#subsription` → `Expenses:Subscriptions`
   - `#health`/`#здоровье` → `Expenses:Health`
   - Места (#Coles, #GYG, #amazon и т.п.) → payee поле, не account
   - Дефолт для неизвестных тегов: `Expenses:Other`

3. **Мультивалюта**: если есть и `idr::` и `aud::`, пишем:
   ```
   2026-01-13 * "Telkomsel"
     Expenses:Subscriptions   52000 IDR @ 0.000X AUD
     Assets:Cash
   ```
   Или если только один `idr::` без `aud::` — просто IDR без конвертации.

4. **Вывод:** `/home/rocky/projects/tools-obsidian/finance/main.beancount`

5. **Верификация:** `bean-check finance/main.beancount` без ошибок; сверить суммы AUD за 1-2 месяца с тем что было в Logseq.

### Веха 0 (оставшееся)
- Git history cleanup (6.3GB → <500MB): требует SSH на Sydney + стоп ботов. Скрипт уже готов концептуально — см. план. Сделать отдельно с координацией.

### Веха 1 — Obsidian конфиг
Создать в `tools-obsidian/obsidian-config/` (НЕ в logseq-content):
- `.obsidian/app.json`, `core-plugins.json`, `community-plugins.json`
- `plugins/periodic-notes/data.json` (путь: `journals/{{date:YYYY}}/YYYY-MM-DD`)
- `plugins/obsidian-git/data.json` (auto-pull/push 30 мин)
- При готовности — скопировать в logseq-content одним коммитом

## Other Notes

### Сервер Sydney
- IP: `217.216.76.5`
- Пользователи: `root` (SSH), `claude` (сервисы)
- Logseq контент: `/home/claude/logseq-content`
- Сервисы: `/home/claude/logseq-services/`
- Immich: `http://localhost:2283`

### Telegram-боты (не трогать)
Всё работает. Боты пишут в `pages/Telegram/` и `journals/`. export-cc пишет `pages/AI - *.md`. photo-bot — `[[Timeline]]` в журналах. gps-bot — порт 8085 на сервере.

### tools-obsidian структура (создана, пустая)
```
~/projects/tools-obsidian/
  finance/     ← сюда beancount файл
  people/      ← сюда people/*.md с frontmatter
  scripts/     ← парсеры и утилиты
  geo/         ← travel.geojson
  courses/     ← курсовые конспекты
  handoffs/    ← этот файл
```
