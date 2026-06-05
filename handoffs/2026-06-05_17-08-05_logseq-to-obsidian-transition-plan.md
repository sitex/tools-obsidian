---
date: 2026-06-05T17:08:05+10:00
researcher: Ivan
git_commit: 305ebe898133a2a287fd4fbbaf8002e7cba763b0
branch: main
repository: tools-obsidian
topic: "Logseq → Obsidian transition: новый vault knowledge-base"
tags: [migration, obsidian, logseq, telegram-bots, vault, transition, handoff]
status: complete
last_updated: 2026-06-05
last_updated_by: Ivan
type: implementation_strategy
---

# Handoff: Переход Logseq → Obsidian (план готов, не запущен)

## Task(s)

Многосессионная миграция Logseq → гибридная архитектура (Obsidian + beancount +
LibreChat/MCP). Главный план: `/home/rocky/.claude/plans/logseq-indexed-engelbart.md`.

**Текущий фокус (сессия 4):** спланирован переход работы из Logseq vault
`logseq-content` в новый Obsidian vault `knowledge-base` по отдельному адресу
(для отката). **План написан и УТВЕРЖДЁН пользователем НЕ был — пользователь
сказал «пока оставь».** План лежит в `/home/rocky/.claude/plans/crystalline-dreaming-taco.md`.

### Статус вех (общий)

| Веха | Статус |
|------|--------|
| 0 — Очистка git-истории | 🔲 Открыт #2 (решится бесплатно при переходе на свежий репо) |
| 1 — Obsidian vault | ✅ Закрыт (#1). tools-obsidian = vault, плагины установлены |
| 2 — beancount | ✅ finance/main.beancount + dashboard.md. Fava #7 ждёт Sydney |
| 3 — Гео | ✅ Артефакты. Dawarich #3 ждёт Sydney |
| 4 — Голос | ✅ scripts/process_voice.py. Деплой #4 ждёт Sydney |
| 5 — Люди | ✅ Закрыт (#5). people/ + index.md |
| 6 — LibreChat+MCP | ✅ Конфиг. Деплой #6 ждёт Sydney |
| Переход на knowledge-base | 📋 План готов, НЕ запущен («пока оставь») |

## Critical References

- **План перехода (главный артефакт этой сессии):** `/home/rocky/.claude/plans/crystalline-dreaming-taco.md`
- **Системный план всех вех:** `/home/rocky/.claude/plans/logseq-indexed-engelbart.md`
- **Прошлый handoff:** `handoffs/2026-06-02_01-30-00_logseq-to-obsidian-migration.md`
- **Источник данных (только чтение):** `/home/rocky/logseq-content/`

## Recent changes

Все коммиты запушены в sitex/tools-obsidian. Рабочее дерево чистое (Obsidian Git
делает auto-commit «vault: auto-commit ...»).

- `thoughts/shared/plans/2026-06-04-migration-session3.md` — план сессии 3 (чекбоксы)
- `CHANGELOG.md` — история сессий 2–3
- `.obsidian/` в корне + плагины (obsidian-git 2.38.3, periodic-notes, dataview 0.5.70, tasks 8.0.0, leaflet 6.0.5)
- `.gitignore:5-8` — добавлены `.obsidian/workspace*.json`, `graph.json`
- `librechat/fava/docker-compose.yml` — Fava для Sydney (#7)
- `projects/index.md` — Dataview-таблица проектов
- `scripts/inventory_block_refs.py` — инвентаризация block-refs (#8 закрыт: в vault 1 ref)

## Learnings

### Боты завязаны на Logseq-формат (главная находка сессии 4)
Исследование `logseq-services/` показало: 4 systemd-бота + 4 cron пишут
**tab-indented Logseq outliner** (`\t\t\t- HH:MM - text`, `[[Timeline]]` как
заголовок, год-подкаталоги `journals/YYYY/`). Парсер `insert_to_timeline` в
`shared/logseq_writer.py` хрупкий — завязан на точное число табов и разделители
`- ---`. **Поэтому решение: гибрид — формат не конвертируем, боты не трогаем.**

### Единая точка переключения пути
Все боты читают `LOGSEQ_DIR` из `shared/config.py:7` (default
`/home/claude/logseq-content`). Переключение vault = одна переменная окружения.
**Исключение:** `gps_bot/file_writer.py:14-15` перечитывает LOGSEQ_DIR
независимо — проверить что env подхвачен.

### Конвейер обработки журнала — в slash-командах vault
Вся логика (DONE-разметка, извлечение `Z - *` подстраниц, сумма расходов) живёт
в `logseq-content/.claude/commands/` (`logseq.md`, `logseq-review.md`,
`export-cc.md`), НЕ в Python-репо. При переносе vault их надо копировать вместе
с `.claude/` и `templates/journal-template.md`.

### История переписки = источник для backfill
`pages/Telegram/Telegram_*.md` — сырой лог сообщений (пишется ботами напрямую),
журнал Timeline — курируемый вывод. Backfill 06:00 replay'ит Telegram_*.md в
журналы. При миграции переносить обязательно.

### Свежий репо решает Веху 0 бесплатно
Новый knowledge-base создаётся со свежей git-историей (commit 1 = текущее
состояние, ~115MB). Раздутые 6.3 ГБ остаются только в архивном logseq-content.

### Решения пользователя по переходу (зафиксированы)
- Формат: **гибрид** (Logseq-формат сейчас, конвертация позже отдельно)
- Vault: **git-репо на ноуте + Sydney**, синхронизация через git
- AI-чаты: **переносить всё** (полная копия)

## Artifacts

- `/home/rocky/.claude/plans/crystalline-dreaming-taco.md` — **план перехода (читать первым)**
- `thoughts/shared/plans/2026-06-04-migration-session3.md` — план сессии 3
- `thoughts/shared/plans/2026-06-04-logseq-to-obsidian-transition.md` — ранний черновик перехода (заменён crystalline-dreaming-taco.md)
- `CHANGELOG.md`
- `handoffs/2026-06-02_01-30-00_logseq-to-obsidian-migration.md` — прошлый handoff
- Скрипты: `scripts/{expenses_to_beancount,migrate_people,generate_geojson,process_voice,generate_dashboard,inventory_block_refs}.py`, `scripts/sync_data_snapshot.sh`
- `librechat/` — docker-compose, librechat.yaml, mcp/beancount_mcp.py, nginx.conf, fava/
- GitHub issues открыты: #2, #3, #4, #6, #7

## Action Items & Next Steps

### Если пользователь решит запустить переход:
Следовать `/home/rocky/.claude/plans/crystalline-dreaming-taco.md` (8 этапов):
1. Создать issue в sitex/tools-obsidian + план в thoughts/shared/plans/
2. `mkdir ~/projects/knowledge-base && git init`
3. `rsync -a --exclude='.git' ~/logseq-content/ ~/projects/knowledge-base/`
4. Влить people/finance/geo/projects/.obsidian из tools-obsidian
5. .gitignore + первый коммит + `gh repo create sitex/knowledge-base`
6. Открыть в Obsidian, проверить
7. Sydney: клонировать, `LOGSEQ_DIR=/home/claude/knowledge-base`, restart ботов
8. Заморозить logseq-content

### Открытый вопрос (не блокирует):
- Телефон: Obsidian Mobile + Obsidian Git или оставить Logseq до стабилизации

### Независимая работа без Sydney (если переход откладывается):
- Деплой на Sydney любой из вех #3/#4/#6/#7 (требует SSH-доступа к 217.216.76.5)

## Other Notes

- **Рабочая директория:** `/home/rocky/projects/tools-obsidian` (= Obsidian vault, открыт)
- **/wf активен:** планы → `thoughts/shared/plans/`, исследования → `thoughts/shared/research/`, задачи → GitHub issue на русском, прогресс комментариями к issue
- **logseq-content .gitignore** был восстановлен до pre-session состояния в сессии 3 (убраны Obsidian/media записи) — НЕ трогать
- **Sydney инфра:** VPS `217.216.76.5`, user `claude`, боты в `/home/claude/logseq-services/`, deploy через `logseq-services/deploy.sh`
- **Obsidian Git** на ноуте делает auto-commit каждые 30 мин — поэтому в логе появляются «vault: auto-commit» коммиты, рабочее дерево обычно чистое
- **memory:** `feedback_logseq_readonly.md` — logseq-content только чтение
