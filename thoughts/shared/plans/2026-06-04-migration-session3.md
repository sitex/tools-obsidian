# Миграция Logseq → гибридная архитектура (сессия 3)

GitHub repo: sitex/tools-obsidian

## Выполнено в сессии 2–3

- [x] Веха 2: beancount парсер + finance/main.beancount (1454 txns) — закрыт
- [x] Веха 1: .obsidian/ задеплоен в корень tools-obsidian (vault = tools-obsidian) — #1 закрыт
- [x] Веха 5: people/ (121 файл) + people/index.md (Dataview CRM) — #5 закрыт
- [x] Веха 4: scripts/process_voice.py (ffmpeg+faster-whisper+роутинг) — #4 скрипт готов
- [x] Веха 6: librechat/ (docker-compose + beancount MCP + nginx) — #6 конфиг готов
- [x] finance/dashboard.md + scripts/generate_dashboard.py
- [x] data/pages/ snapshot (189 стр.) + scripts repo-relative
- [x] scripts/sync_data_snapshot.sh
- [x] scripts/inventory_block_refs.py — 13 refs, все разрешены (#8)
- [x] librechat/fava/docker-compose.yml (#7)
- [x] projects/index.md
- [x] CHANGELOG.md
- [x] Obsidian установлен (flatpak), плагины скачаны
- [x] logseq-content .gitignore — откат Obsidian/media записей
- [x] .gitignore tools-obsidian — ignore workspace.json

## Открытые задачи

- [ ] #8 Конвертация block-refs: написать scripts/convert_block_refs.py (13 штук, все разрешены)
- [ ] #7 Fava: деплой на Sydney (`scp librechat/fava/ claude@217.216.76.5:~/fava/ && docker compose up -d`)
- [ ] #4 Голос: интеграция process_voice.py с Telegram-ботом на Sydney
- [ ] #6 LibreChat: деплой на Sydney (заполнить .env, настроить nginx Tailscale hostname)
- [ ] #3 Dawarich: установка Docker на Sydney, поток OwnTracks
- [ ] #2 Очистка git-истории logseq-content (6.3 GB → <500 MB) — требует стоп ботов + force-push
