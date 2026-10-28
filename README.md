# Job Tracker API

Ein Web-Service zur Verwaltung von Bewerbungsprozessen, umgesetzt mit FastAPI, SQLAlchemy und einem minimalistischen JavaScript-Dashboard.

## Features

- REST API mit vollständiger CRUD-Funktionalität
- Datenbank-Persistenz über SQLAlchemy (SQLite)
- Datenvalidierung mit Pydantic Schemas
- Interaktives Dashboard (HTML/CSS/JS)
- Automatisch generierte OpenAPI-Dokumentation (`/docs`)

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, Pydantic, Uvicorn
- **Datenbank:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Projektstruktur

```text
job-tracker-api/
├── app/
│   ├── static/
│   │   ├── app.js
│   │   ├── index.html
│   │   └── style.css
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       └── applications.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup & Start

1. Repository klonen & Umgebung einrichten:

```bash
git clone <repository-url>
cd job-tracker-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```
3. Server starten:
```bash
uvicorn app.main:app --reload
```