---
date: 2026-06-02T01:30:00+10:00
researcher: Ivan
git_commit: 49db383
branch: main
repository: tools-obsidian
topic: "Logseq → Obsidian + beancount + LibreChat migration"
tags: [migration, obsidian, beancount, logseq, people, geo, librechat, mcp, voice]
status: in_progress
last_updated: 2026-06-02
last_updated_by: Claude
type: implementation_strategy
---

# Handoff: Миграция Logseq → гибридная архитектура (сессия 3)

## Task(s)

Продолжение поэтапной миграции с Logseq на гибридную систему.

### Статус вех

| Веха | Статус | Описание |
|------|--------|----------|
| 0 — Гигиена | 🔲 Отложено | Очистка git-истории (6.3 GB) — требует координации Sydney |
| 1 — Obsidian | ⏳ Ждёт деплоя | Конфиг готов в `obsidian-config/`. Деплой: `cp -r obsidian-config/.obsidian ~/logseq-content/` |
| 2 — beancount | ✅ Выполнено | `finance/main.beancount` (1454 txns) + `finance/dashboard.md` (avg A$2752/мес) |
| 3 — Гео | ✅ Артефакты | `geo/travel.geojson` (69 features, 42 с coords). Dawarich — следующий шаг (Sydney) |
| 4 — Голос/курсы | ✅ Скрипт готов | `scripts/process_voice.py` — ffmpeg+faster-whisper+роутинг. Нужен деплой на Sydney |
| 5 — Люди/проекты | ⏳ Ждёт деплоя | `people/` (121 файл) + `people/index.md` (Dataview CRM). Деплой: `cp -r people/ ~/logseq-content/people/` |
| 6 — LibreChat+MCP | ✅ Конфиг готов | `librechat/` — docker-compose + beancount MCP сервер + nginx. Нужен деплой на Sydney |

## Critical References

- **Главный план:** `/home/rocky/.claude/plans/logseq-indexed-engelbart.md`
- **GitHub repo:** `https://github.com/sitex/tools-obsidian`
- **Источник данных:** `/home/rocky/logseq-content/` — **только чтение**
- **Snapshot данных:** `data/pages/` — 189 страниц (Expenses.md + люди + локации), обновлять через `scripts/sync_data_snapshot.sh`

## Recent changes (сессия 3)

### Новые артефакты
- `scripts/process_voice.py` — голосовой пайплайн: OGG→WAV (ffmpeg loudnorm+arnndn) → faster-whisper → роутинг по хэштегу (#fin/#person/#project/default journal)
- `scripts/generate_dashboard.py` — beancount 3.x Python API → `finance/dashboard.md` (monthly trend, top categories, multi-currency)
- `finance/dashboard.md` — текущий дашборд (1454 txns, avg A$2752/мес, топ: Shopping A$12738)
- `librechat/docker-compose.yml` — LibreChat latest + MongoDB 7 + Meilisearch, порт 127.0.0.1:3080
- `librechat/librechat.yaml` — MCP серверы: filesystem-mcp (/vault) + beancount-mcp (python3 /mcp/beancount_mcp.py)
- `librechat/mcp/beancount_mcp.py` — MCP stdio JSON-RPC: `query_expenses`, `get_monthly_totals`
- `librechat/nginx.conf` — reverse proxy + WebSocket для Tailscale
- `librechat/.env.example` — переменные (ANTHROPIC_API_KEY, JWT_SECRET, MEILI_MASTER_KEY)
- `data/pages/` — 189 исходных страниц (snapshot logseq-content, 1.1MB), скрипты переведены на этот путь
- `scripts/sync_data_snapshot.sh` — обновление snapshot из live logseq-content
- `people/index.md` — Dataview CRM-таблица (все контакты + недавние + без даты)

### Изменения скриптов
- `scripts/expenses_to_beancount.py`, `migrate_people.py`, `generate_geojson.py` — пути теперь `Path(__file__).parent.parent / "data/pages"` (не хардкод logseq-content)

### Откаты
- `logseq-content/.gitignore` — восстановлен до pre-session состояния (удалены Obsidian/media записи)

## Learnings

### Ключевые ограничения (не изменились)
- **logseq-content — только чтение.** Все инструменты и файлы — в tools-obsidian.
- **data/pages/** — snapshot для автономной работы скриптов. Обновлять через `sync_data_snapshot.sh` когда меняются source pages в logseq-content.

### beancount 3.x
- `bean-query` удалён. Использовать Python API: `from beancount import loader; from beancount.core import data`
- `bean-check` и `bean-format` — единственные CLI инструменты в /home/rocky/.local/bin/bean-*

### LibreChat MCP (из документации)
- MCP серверы конфигурируются в `librechat.yaml` под ключом `mcpServers`
- stdio transport: команда запускается как subprocess, JSON-RPC 2.0 через stdin/stdout
- Нужен обработчик `initialize` + `tools/list` + `tools/call` (минимум)

### process_voice.py
- faster-whisper нужно устанавливать отдельно: `pip install faster-whisper`
- arnndn модель (rnnoise) — опциональна, fallback на `highpass=f=80,afftdn=nf=-25`
- OGG файлы от Telegram боты сохраняют как `.oga` или `.ogg` — оба формата работают через ffmpeg

## Artifacts

### Скрипты (tools-obsidian/scripts/)
- `expenses_to_beancount.py` — Expenses.md → beancount (читает data/pages/)
- `migrate_people.py` — person pages → people/ (читает data/pages/)
- `generate_geojson.py` — location pages → geo/travel.geojson (читает data/pages/)
- `process_voice.py` — OGG → транскрипт → vault entry
- `generate_dashboard.py` — beancount → finance/dashboard.md
- `sync_data_snapshot.sh` — обновить data/pages/ из logseq-content

### Данные (tools-obsidian/)
- `finance/main.beancount` — 1454 транзакции
- `finance/dashboard.md` — дашборд (avg A$2752/мес)
- `people/` — 122 файла (121 + index.md)
- `geo/travel.geojson` — 69 features
- `data/pages/` — 189 страниц-источников

### LibreChat (tools-obsidian/librechat/)
- `docker-compose.yml`, `librechat.yaml`, `mcp/beancount_mcp.py`, `nginx.conf`, `.env.example`

### GitHub Issues (sitex/tools-obsidian)
- #1 — Веха 1: Деплой Obsidian конфига (ждёт пользователя)
- #2 — Веха 0: Очистка git-истории (отложено, нужен Sydney)
- #3 — Веха 3: Dawarich (артефакты готовы, нужен Sydney)
- #4 — Веха 4: Голосовой пайплайн (скрипт готов, нужен деплой Sydney)
- #5 — Веха 5: Люди/проекты (артефакты + index.md готовы, ждёт пользователя)
- #6 — Веха 6: LibreChat + MCP (конфиг готов, нужен деплой Sydney)

## Action Items & Next Steps

### Пользователь делает сам (без Claude):
1. **Веха 1:** `cp -r ~/projects/tools-obsidian/obsidian-config/.obsidian ~/logseq-content/` → Obsidian → Trust plugins
2. **Веха 5:** `rm ~/projects/tools-obsidian/people/CC---*.md && cp -r ~/projects/tools-obsidian/people/ ~/logseq-content/people/`

### Деплой на Sydney (SSH):
3. **Веха 4:** `pip install faster-whisper` + интеграция `process_voice.py` с Telegram-ботом (передавать путь к OGG)
4. **Веха 6:** скопировать `librechat/` на Sydney, заполнить `.env`, обновить `nginx.conf` с реальным Tailscale hostname, `docker compose up -d`
5. **Веха 3:** установить Dawarich Docker, настроить поток OwnTracks

### Следующая независимая работа (без Sydney):
6. **Веха 0 — инвентаризация block-refs:** найти 381 `((uuid))` в logseq-content/pages/, построить карту uuid→файл:строка для последующей конвертации в Obsidian-синтаксис `[[page#^blockid]]`
7. **finance:** Fava docker-compose для Sydney (веб-морда beancount за Tailscale)
8. **projects/index.md:** Dataview-таблица проектов (аналог people/index.md)
9. **Обновить data/ snapshot:** если proshло время → `scripts/sync_data_snapshot.sh`

### Требует координации с Sydney:
10. **Веха 0:** Полная очистка git-истории: стоп ботов → `git filter-repo` → force-push → переклонирование на Sydney и телефоне

## Other Notes

### Деплой LibreChat на Sydney — детали
1. `scp -r ~/projects/tools-obsidian/librechat/ claude@217.216.76.5:~/librechat/`
2. На сервере: `cp .env.example .env`, заполнить ANTHROPIC_API_KEY (из claude.ai/settings) и сгенерировать JWT-ключи: `openssl rand -hex 32`
3. Tailscale hostname: `tailscale status | head -3` → вставить в nginx.conf вместо TAILSCALE_HOSTNAME
4. Проверить пути: `/home/claude/logseq-content` → если не так, исправить volumes в docker-compose.yml
5. `docker compose up -d`

### people/ — 2 файла-мусора
`CC---logseq-spa-research-...` и `CC---write-Claude-instructions-...` — AI-чаты случайно попали через тег #человек. Удалить перед деплоем в logseq-content.

### Структура tools-obsidian
```
~/projects/tools-obsidian/
  data/pages/      ← 189 source pages snapshot (обновлять через sync_data_snapshot.sh)
  finance/         ← main.beancount + dashboard.md
  geo/             ← travel.geojson
  librechat/       ← docker-compose, librechat.yaml, mcp/, nginx.conf
  obsidian-config/ ← .obsidian/ для деплоя в logseq-content
  people/          ← 122 файла (121 + index.md)
  scripts/         ← 6 скриптов
  handoffs/        ← этот файл
```
