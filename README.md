<div align="center">

# CineLog

**[English](#english) · [Español](#español)**

![HTML](https://img.shields.io/badge/HTML-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-white?style=flat)

**Personal movie & series tracker · Registro personal de películas y series**

</div>

---

## English

A personal movie and series tracker with a minimal dark interface. Log titles, rate them, write notes, and track your watch status — all stored locally in the browser with no backend required. Includes an optional REST API built with FastAPI and SQLite for persistent server-side storage.

### Features

- **Zero-dependency frontend** — single HTML file, no framework, no build step. Open it in a browser and it works
- **Local persistence** — all data stored in `localStorage`, survives page refreshes without a server
- **Full CRUD** — add, filter, and remove titles from your log
- **Watch status** — mark titles as `watched`, `pending`, or `dropped`
- **Live stats** — total, watched count, pending count, and average rating update in real time
- **Bilingual UI** — toggle between English and Spanish with one click
- **Optional REST API** — FastAPI backend with SQLite, full CRUD endpoints, and auto-generated Swagger docs at `/docs`

### Project Structure

```
cinelog/
├── index.html        ← Standalone frontend, no server needed
├── main.py           ← FastAPI backend (optional)
├── models.py         ← SQLModel table definitions
├── database.py       ← SQLite engine and session setup
├── requirements.txt  ← Python dependencies (API only)
└── README.md
```

### Run the frontend

Open `index.html` in any browser. No install, no server, no setup.

### Run the API (optional)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API at `http://localhost:8000` · Docs at `http://localhost:8000/docs`

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/titles` | List all titles (supports filters) |
| `GET` | `/titles/{id}` | Get a single title |
| `POST` | `/titles` | Add a new title |
| `PUT` | `/titles/{id}` | Update a title |
| `DELETE` | `/titles/{id}` | Delete a title |
| `GET` | `/stats` | Counts by status, average rating, top rated |

### Tech

HTML · CSS · JavaScript · localStorage · Python · FastAPI · SQLModel · SQLite · Uvicorn

---

## Español

Registro personal de películas y series con una interfaz oscura minimalista. Agrega títulos, califícalos, escribe notas y lleva el control de lo que has visto — todo guardado en el navegador sin necesidad de un servidor. Incluye una API REST opcional con FastAPI y SQLite para almacenamiento persistente del lado del servidor.

### Características

- **Frontend sin dependencias** — un solo archivo HTML, sin framework ni build. Ábrelo en el navegador y funciona
- **Persistencia local** — todos los datos en `localStorage`, sobrevive recargas sin servidor
- **CRUD completo** — agrega, filtra y elimina títulos de tu registro
- **Estado de visto** — marca títulos como `watched`, `pending` o `dropped`
- **Estadísticas en vivo** — total, vistos, pendientes y promedio se actualizan en tiempo real
- **UI bilingüe** — cambia entre inglés y español con un clic
- **API REST opcional** — backend FastAPI con SQLite, endpoints CRUD completos y docs autogeneradas en `/docs`

### Estructura

```
cinelog/
├── index.html        ← Frontend standalone, no necesita servidor
├── main.py           ← Backend FastAPI (opcional)
├── models.py         ← Definición de tablas con SQLModel
├── database.py       ← Motor SQLite y configuración de sesión
├── requirements.txt  ← Dependencias Python (solo API)
└── README.md
```

### Ejecutar el frontend

Abre `index.html` en cualquier navegador. Sin instalación, sin servidor, sin configuración.

### Ejecutar la API (opcional)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API en `http://localhost:8000` · Docs en `http://localhost:8000/docs`

### Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/titles` | Lista todos los títulos (soporta filtros) |
| `GET` | `/titles/{id}` | Obtiene un título por ID |
| `POST` | `/titles` | Agrega un nuevo título |
| `PUT` | `/titles/{id}` | Actualiza un título |
| `DELETE` | `/titles/{id}` | Elimina un título |
| `GET` | `/stats` | Conteos por estado, promedio, top calificados |

### Tecnologías

HTML · CSS · JavaScript · localStorage · Python · FastAPI · SQLModel · SQLite · Uvicorn

---

<div align="center">
MIT License · Made by <a href="https://github.com/privatednicolas">privatednicolas</a>
</div>
