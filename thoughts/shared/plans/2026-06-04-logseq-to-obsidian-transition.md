# План перехода Logseq → Obsidian

## Исходная ситуация

- `logseq-content/` — живой vault: 3956 реальных страниц + 2625 AI-чатов + 1498 журналов
- Боты пишут в Logseq-формат (буллеты + `key:: value`). Путь задан одной переменной: `LOGSEQ_DIR=/home/claude/logseq-content`
- `tools-obsidian/` — новый vault: Obsidian сконфигурирован, people/, finance/, geo/

## Ключевое решение: новый адрес данных

**Цель:** vault в новом репо, logseq-content остаётся нетронутым как архив с возможностью отката.

Новый vault: `~/projects/knowledge-base/` (отдельный git-репо)

```
~/projects/knowledge-base/        ← новый Obsidian vault
  journals/YYYY/YYYY-MM-DD.md     ← перенесено из logseq-content
  pages/                          ← реальные страницы (без AI-чатов)
  people/                         ← из tools-obsidian
  finance/                        ← из tools-obsidian
  geo/                            ← из tools-obsidian
  .obsidian/                      ← из tools-obsidian

~/logseq-content/                 ← заморожен, только чтение, архив
~/projects/tools-obsidian/        ← инструменты, скрипты, остаётся
```

## Этапы

### Этап 0 — Подготовка (без деструктивных действий)
- [ ] Очистить git-историю logseq-content (Веха 0: 6.3GB → <500MB) — опционально, можно после
- [ ] Финальный `git pull` logseq-content на всех устройствах (ноут, Sydney, телефон)

### Этап 1 — Создать новый репо knowledge-base

```bash
mkdir ~/projects/knowledge-base && cd ~/projects/knowledge-base
git init
gh repo create sitex/knowledge-base --private --source=. --push
```

### Этап 2 — Перенести контент

**Журналы** (8.5MB, полностью):
```bash
cp -r ~/logseq-content/journals/ ~/projects/knowledge-base/journals/
```

**Реальные страницы** (без AI-чатов, ~18MB):
```bash
find ~/logseq-content/pages/ -name "*.md" ! -name "AI - *" \
  -exec cp {} ~/projects/knowledge-base/pages/ \;
```

**AI-чаты** — НЕ переносить. Остаются в logseq-content как архив.

**Из tools-obsidian** — уже готово:
```bash
cp -r ~/projects/tools-obsidian/people/   ~/projects/knowledge-base/
cp -r ~/projects/tools-obsidian/finance/  ~/projects/knowledge-base/
cp -r ~/projects/tools-obsidian/geo/      ~/projects/knowledge-base/
cp -r ~/projects/tools-obsidian/.obsidian/ ~/projects/knowledge-base/
```

### Этап 3 — Настроить .gitignore нового репо

```
# Obsidian per-device state
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/graph.json

# Logseq
logseq/bak/

# Media (хранятся в Immich / на сервере)
*.mp3 *.mp4 *.wav *.ogg *.flac *.mov *.mkv
*.jpg *.jpeg *.png *.gif *.webp
```

### Этап 4 — Переключить ботов (одна строка)

Все боты читают `LOGSEQ_DIR` из `shared/config.py`:
```python
LOGSEQ_DIR = Path(os.getenv("LOGSEQ_DIR", "/home/claude/logseq-content"))
```

На Sydney:
```bash
# В systemd unit или .env:
LOGSEQ_DIR=/home/claude/knowledge-base
```

Одно изменение — все боты переключаются. **Откат**: вернуть переменную.

### Этап 5 — Открыть vault в Obsidian

Obsidian → Open folder as vault → `~/projects/knowledge-base`

### Этап 6 — Заморозить logseq-content

```bash
# Сделать read-only локально (опционально)
chmod -R a-w ~/logseq-content/
# Архивный remote на GitHub остаётся
```

## Что НЕ нужно конвертировать

Logseq-формат (`- буллеты`, `key:: value`) **читается Obsidian нативно** — буллеты как списки, свойства как plain text. Жёсткой конвертации нет.

Единственное что не работает в Obsidian из Logseq-синтаксиса:
- `((uuid))` block-refs → в knowledge-base будет 0–1 штука (не критично)
- `{{query ...}}` DataLog-запросы → заменяются Dataview (уже настроен)
- `#+BEGIN_QUERY` блоки → то же

## Откат

| Сценарий | Действие |
|----------|----------|
| Боты пишут не туда | `LOGSEQ_DIR=/home/claude/logseq-content` — мгновенно |
| Obsidian сломал файл | `git checkout` в knowledge-base |
| Весь переход провалился | logseq-content не тронут, открыть в Logseq как раньше |

## Риски и решения

| Риск | Решение |
|------|---------|
| Дублирование people/ между tools-obsidian и knowledge-base | tools-obsidian остаётся источником скриптов, knowledge-base — живые данные |
| Боты на Sydney — нужен deploy | Один `systemctl edit` + `restart` |
| Телефон — Working Copy / Obsidian Mobile | Клонировать knowledge-base, настроить Obsidian Git |
| AI-чаты (2625 файлов) не перенесены | Открывать logseq-content для поиска по архиву |

## Вопросы перед стартом

1. **Когда переключать ботов?** — можно параллельно (боты пишут в logseq-content, Obsidian читает knowledge-base) или сразу
2. **Телефон:** Obsidian Mobile + Obsidian Git или оставить Logseq на телефоне?
3. **Очистка git-истории** (6.3GB) делать до или после переноса?

## Что уже готово

- [x] Obsidian установлен (flatpak 1.12.7)
- [x] .obsidian/ конфиг с 5 плагинами в tools-obsidian
- [x] people/, finance/, geo/ — структурированные данные в tools-obsidian
- [x] Боты имеют единую точку переключения (LOGSEQ_DIR)
