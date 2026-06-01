# Changelog

## [Unreleased]

## [Session 3] — 2026-06-02

### Added
- `scripts/process_voice.py` — голосовой пайплайн: OGG → ffmpeg (loudnorm+arnndn) → faster-whisper → роутинг по хэштегу (#fin/#person/#project → vault) [#4]
- `scripts/generate_dashboard.py` — beancount 3.x → `finance/dashboard.md` (monthly trend, top categories, multi-currency)
- `scripts/inventory_block_refs.py` — инвентаризация `((uuid))` block-refs, результат: 13 refs, все разрешены [#8]
- `scripts/sync_data_snapshot.sh` — обновление `data/pages/` snapshot из live logseq-content
- `librechat/docker-compose.yml` + `librechat.yaml` + `mcp/beancount_mcp.py` + `nginx.conf` — LibreChat + MCP [#6]
- `librechat/fava/docker-compose.yml` — Fava веб-морда beancount для Sydney [#7]
- `finance/dashboard.md` — сгенерированный дашборд (avg A$2752/мес, топ: Shopping)
- `data/pages/` — 189 страниц snapshot (Expenses.md + люди + локации, 1.1MB) для автономной работы скриптов
- `people/index.md` — Dataview CRM-таблица (все / недавние / без даты контакта)
- `projects/index.md` — Dataview таблица проектов
- `.obsidian/` в корне репо — tools-obsidian теперь Obsidian vault [#1]
- Community плагины: obsidian-git 2.38.3, periodic-notes 1.0.0-beta.3, dataview 0.5.70, tasks 8.0.0, leaflet 6.0.5

### Changed
- `scripts/expenses_to_beancount.py`, `migrate_people.py`, `generate_geojson.py` — пути теперь repo-relative (`data/pages/`), не хардкод logseq-content
- `.gitignore` — добавлены `.obsidian/workspace.json`, `workspace-mobile.json`, `graph.json`

### Fixed
- `logseq-content/.gitignore` — восстановлен до pre-session состояния (убраны Obsidian/media записи)

### Closed
- #1 Веха 1: Obsidian vault — tools-obsidian открывается как vault напрямую
- #5 Веха 5: Люди/проекты — people/ уже в tools-obsidian (vault)

---

## [Session 2] — 2026-06-01

### Added
- `scripts/expenses_to_beancount.py` — парсер Logseq Expenses.md → beancount
- `finance/main.beancount` — 1454 транзакции (май 2025 — июнь 2026), bean-check чистый
- `scripts/migrate_people.py` — person pages → `people/` с YAML frontmatter
- `people/` — 121 файл (name, location, tags, last_contact, description)
- `scripts/generate_geojson.py` — location pages → GeoJSON
- `geo/travel.geojson` — 69 features (42 с координатами)
- `obsidian-config/.obsidian/` — конфиг vault (app, plugins, periodic-notes, git)
- `obsidian-config/DEPLOY.md` — инструкция деплоя (устарела после Session 3)
- `handoffs/` — документы передачи контекста между сессиями
