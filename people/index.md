---
title: Люди
tags: [index, crm]
---

# Люди

```dataview
TABLE
  location AS "Где",
  last_contact AS "Посл. контакт",
  tags AS "Теги"
FROM "people"
WHERE file.name != "index"
SORT last_contact DESC
```

---

## Недавние контакты

```dataview
TABLE
  last_contact AS "Дата",
  location AS "Где"
FROM "people"
WHERE file.name != "index" AND last_contact != null
SORT last_contact DESC
LIMIT 10
```

---

## Без даты контакта

```dataview
LIST
FROM "people"
WHERE file.name != "index" AND last_contact = null
SORT file.name ASC
```
