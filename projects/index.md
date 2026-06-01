---
title: Проекты
tags: [index, projects]
---

# Проекты

```dataview
TABLE
  status AS "Статус",
  tags AS "Теги",
  file.mtime AS "Изменён"
FROM "projects"
WHERE file.name != "index"
SORT file.mtime DESC
```
