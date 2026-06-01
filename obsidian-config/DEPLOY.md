# Деплой Obsidian-конфига в logseq-content

## Что делает этот конфиг

Настраивает logseq-content как Obsidian vault:
- **Periodic Notes** — ежедневные журналы в `journals/YYYY/YYYY-MM-DD.md` (совпадает с текущим форматом Logseq)
- **Obsidian Git** — auto-pull при старте, auto-commit/push каждые 30 мин
- **Dataview** — запросы по frontmatter (таблицы людей, проектов)
- **Tasks** — задачи в заметках
- **Leaflet** — карты из `geo/travel.geojson`

## Шаги деплоя

### 1. Скопировать конфиг

```bash
cp -r ~/projects/tools-obsidian/obsidian-config/.obsidian ~/logseq-content/
```

Проверить что `.gitignore` в logseq-content уже содержит:
```
.obsidian/workspace*.json
```
Если нет — добавить (иначе workspace будет конфликтовать между устройствами).

### 2. Открыть vault в Obsidian

Файл → Открыть папку как vault → `~/logseq-content`

### 3. Установить плагины

Obsidian предложит установить отсутствующие community plugins автоматически.
Если нет — вручную в Settings → Community Plugins:

| ID | Название |
|----|---------|
| `obsidian-git` | Obsidian Git |
| `periodic-notes` | Periodic Notes |
| `dataview` | Dataview |
| `obsidian-tasks-plugin` | Tasks |
| `obsidian-leaflet` | Obsidian Leaflet |

После установки плагинов их config (`data.json`) уже готов — дополнительной настройки не требуется.

### 4. Проверить Obsidian Git

В Settings → Obsidian Git:
- Auto-pull on startup: ✓
- Auto-commit/push interval: 30 min
- Pull method: rebase (важно — совпадает с `git-sync-debounce`)

### 5. Проверить Periodic Notes

В Settings → Periodic Notes → Daily Notes:
- Format: `YYYY-MM-DD`
- Folder: `journals/{{date:YYYY}}`

Нажать "Open today's daily note" — должен открыться существующий файл в `journals/2026/`.

## Коммит в logseq-content

После проверки — закоммитить одним коммитом:
```bash
cd ~/logseq-content
git add .obsidian/
git commit -m "Add Obsidian vault config (Milestone 1)"
```

## Мобильный доступ

Obsidian Mobile + Working Copy / Obsidian Git на тот же клон.
Настройки синхронизируются через `.obsidian/` в git.
`workspace*.json` исключён из git — у каждого устройства свой workspace.
