---
date: 2026-06-02T00:51:22+10:00
researcher: Ivan
git_commit: 3499116
branch: main
repository: tools-obsidian
topic: "Logseq → Obsidian + beancount + LibreChat migration"
tags: [migration, obsidian, beancount, logseq, people, geo, librechat, mcp]
status: in_progress
last_updated: 2026-06-02
last_updated_by: Claude
type: implementation_strategy
---

# Handoff: Миграция Logseq → гибридная архитектура (сессия 2)

## Task(s)

Продолжение поэтапной миграции с Logseq на гибридную систему.

### Статус вех

| Веха | Статус | Описание |
|------|--------|----------|
| 0 — Гигиена | ✅ Частично | IP починен, webhook восстановлен. Очистка git-истории (6.3 GB) — отдельная задача |
| 1 — Obsidian | ✅ Готово к деплою | Конфиг создан в `obsidian-config/`, деплоит пользователь сам |
| 2 — beancount | ✅ Выполнено | Парсер + `finance/main.beancount` (1454 транзакции, bean-check чистый) |
| 3 — Гео | ✅ Артефакты готовы | `geo/travel.geojson` создан (44 geolocated features). Dawarich — отдельно |
| 4 — Голос/курсы | 🔲 Не начато | |
| 5 — Люди/проекты | ✅ Артефакты готовы | `people/` (121 файл с YAML frontmatter). Нужен деплой в logseq-content |
| 6 — LibreChat+MCP | 🔲 Не начато | |

## Critical References

- **Главный план:** `/home/rocky/.claude/plans/logseq-indexed-engelbart.md` — полный системный дизайн всех 7 вех
- **GitHub repo:** `https://github.com/sitex/tools-obsidian` — все инструменты и артефакты здесь
- **Источник данных:** `/home/rocky/logseq-content/` — **только чтение**, не модифицировать

## Recent changes

Все изменения — в `tools-obsidian` (GitHub: sitex/tools-obsidian).

### Веха 2 — beancount
- `scripts/expenses_to_beancount.py` — парсер Logseq Expenses.md → beancount
- `finance/main.beancount` — 1454 транзакции, май 2025 — июнь 2026

### Веха 1 — Obsidian конфиг
- `obsidian-config/.obsidian/app.json` — core settings, wikilinks, live preview
- `obsidian-config/.obsidian/core-plugins.json` — включённые core plugins
- `obsidian-config/.obsidian/community-plugins.json` — obsidian-git, periodic-notes, dataview, tasks, leaflet
- `obsidian-config/.obsidian/plugins/obsidian-git/data.json` — auto-pull/push 30 мин, rebase
- `obsidian-config/.obsidian/plugins/periodic-notes/data.json` — format YYYY-MM-DD, folder `journals/{{date:YYYY}}`
- `obsidian-config/DEPLOY.md` — инструкция по деплою

### Веха 5 — люди
- `scripts/migrate_people.py` — читает logseq-content/pages/ (только чтение), пишет в `people/`
- `people/` — 121 файл с YAML frontmatter (name, location, tags, last_contact, description)

### Веха 3 — гео
- `scripts/generate_geojson.py` — читает location pages, генерирует geojson
- `geo/travel.geojson` — 71 feature (44 с координатами), маршрут + POI

### logseq-content (минимальные изменения)
- `.gitignore` — убрана строка `.obsidian/plugins/obsidian-git/data.json` (был auto-committed)

## Learnings

### Ключевые ограничения
- **logseq-content — только чтение.** Пользователь запретил любые модификации. Все инструменты и файлы — в tools-obsidian. Деплой пользователь делает сам командой `cp`.
- **logseq-content/.gitignore** уже содержит строки для Obsidian workspace и медиа (были добавлены ранее, до этой сессии).

### Формат Expenses.md (для парсера)
```
- ## 2026                    ← год (Logseq outline, не markdown)
  - ### January              ← месяц
    - [[2026-01-01]]         ← дата-блок (2 tabs)
      id:: <uuid>
      collapsed:: true
        - #category [#payee] Description    ← item (3 tabs)
          currency:: amount                  ← свойство (3 tabs + 2 spaces)
```
- Файл с CRLF (`\r\n`), `splitlines()` обрабатывает корректно
- Item'ы бывают без `#` (plain text) — парсер должен их ловить
- `aud::` на уровне date-блока = дневной итог (игнорировать, не создавать транзакцию)
- Multi-currency: foreign + aud → записать AUD с комментарием `;  X FOREIGN` (избегает rounding errors beancount 3.x)
- beancount 3.x: `@@` total-cost operator конвертируется в `@` unit-cost, что даёт tiny float errors

### Журналы в logseq-content
- Структура: `journals/YYYY/YYYY-MM-DD.md` (год-подкаталоги)
- Obsidian Periodic Notes настроен точно под этот формат — отдельных журналов создаваться не будет

### GitHub
- `tools-obsidian` репозиторий создан: `git@github.com:sitex/tools-obsidian.git`
- Все 6 issue по вехам созданы там
- В logseq-content issues закрыты (были дубли)

### Сервисная инфраструктура (для справки, не трогать)
- Боты живут в `~/projects/logseq-services/`
- Sydney сервер: `217.216.76.5`, user `claude`
- webhook-server на порту 8080 управляется systemd
- git-sync-debounce делает auto-commit с именем "Logseq: auto-commit HH:MM"

## Artifacts

### Скрипты (tools-obsidian/scripts/)
- `scripts/expenses_to_beancount.py` — Logseq Expenses.md → beancount
- `scripts/migrate_people.py` — person pages → people/ с YAML frontmatter
- `scripts/generate_geojson.py` — location pages → geo/travel.geojson

### Данные (tools-obsidian/)
- `finance/main.beancount` — 1454 транзакции, AUD/IDR/USD/RUB/KZT
- `people/` — 121 файл (ASMY-*, Vera, Benjamin, кириллица, etc.)
- `geo/travel.geojson` — travel route LineString + 40 point features

### Obsidian конфиг (tools-obsidian/obsidian-config/)
- `.obsidian/app.json`, `core-plugins.json`, `community-plugins.json`, `appearance.json`
- `.obsidian/plugins/obsidian-git/data.json`
- `.obsidian/plugins/periodic-notes/data.json`
- `.obsidian/plugins/dataview/data.json`
- `.obsidian/plugins/obsidian-tasks-plugin/data.json`
- `.obsidian/plugins/obsidian-leaflet/data.json`
- `DEPLOY.md` — инструкция деплоя

### GitHub Issues (sitex/tools-obsidian)
- #1 — Веха 1: Деплой Obsidian конфига
- #2 — Веха 0: Очистка git-истории (6.3 GB)
- #3 — Веха 3: Dawarich + geo (артефакты готовы, Dawarich — следующий шаг)
- #4 — Веха 4: Голосовой пайплайн
- #5 — Веха 5: Люди/проекты (артефакты готовы, деплой — следующий шаг)
- #6 — Веха 6: LibreChat + MCP

## Action Items & Next Steps

### Если пользователь готов задеплоить:
1. **Веха 1 (Obsidian):** `cp -r ~/projects/tools-obsidian/obsidian-config/.obsidian ~/logseq-content/` → открыть vault → установить плагины
2. **Веха 5 (люди):** Пересмотреть `people/` → скопировать в logseq-content → настроить Dataview-таблицу

### Следующая независимая работа (без доступа к Sydney):
3. **Веха 6 — LibreChat/MCP подготовка:** Написать конфиг docker-compose для LibreChat, схему MCP-серверов (filesystem-mcp, beancount-mcp)
4. **Веха 4 — Голосовой пайплайн:** Написать скрипт обработки голосовых из Telegram (`scripts/process_voice.py`): ffmpeg тюнинг → faster-whisper → роутинг по хэштегу
5. **finance/dashboard.md:** Написать скрипт генерации финансового дашборда из beancount (агрегаты по категориям, monthly trend)

### Требует координации с Sydney:
6. **Веха 0:** Очистка git-истории logseq-content (стоп ботов → filter-repo → force-push → переклонирование)
7. **Веха 3:** Установка Dawarich Docker, настройка потока OwnTracks

## Other Notes

### Что точно работает в beancount парсере
- Верификация: суммы AUD по месяцам совпадают с raw Logseq (расхождения ≤ объяснены)
- Август 2025 — декабрь 2025: расхождение = income items (не Expenses:*, правильно)
- Апрель 2026: расхождение 116.80 = дневной итог на date-блоке (правильно игнорируется)
- bean-check 0 errors (beancount 3.2.3)

### Данные people/ — качество
- 2 файла попали случайно: `CC---logseq-spa-research-and-improvements-20260423.md` и `CC---write-Claude-instructions-to-file-20260130.md` — это AI-чаты с тегом #человек, можно удалить
- Часть людей без `last_contact` — у них не было дат в странице
- Stella.md содержит личные данные (телефон, физические характеристики) — пользователь должен решить оставлять ли в git

### Структура tools-obsidian
```
~/projects/tools-obsidian/
  finance/      ← main.beancount
  people/       ← 121 файл с frontmatter
  scripts/      ← 3 парсера
  geo/          ← travel.geojson
  obsidian-config/  ← .obsidian/ для деплоя
  handoffs/     ← этот файл
```

### Источник данных
- Expenses.md: `/home/rocky/logseq-content/pages/Expenses.md` (4691 строк)
- Person pages: `/home/rocky/logseq-content/pages/*.md` (121 из 6555 = person)
- Location pages: 68 страниц с `#место` или `Тип:: Город/Страна`
- Journals: `/home/rocky/logseq-content/journals/YYYY/YYYY-MM-DD.md`
