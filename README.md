<div align="center">

# cinelog-api

**[English](#english) · [Español](#español)**

![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-009688?style=flat&logo=fastapi&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-white?style=flat)

**REST API for personal movie & series tracking · API REST para registro personal de películas y series**

</div>

---

## English

A REST API built with FastAPI for logging and rating movies and series. Think of it as a minimal personal Letterboxd — add titles, write notes, assign a rating, and mark them as watched or pending. Fully documented via the auto-generated Swagger UI at `/docs`.

### Features

- **Full CRUD** — create, read, update, and delete entries for movies and series
- **Rating system** — score each title from 1 to 10 with an optional personal note
- **Status tracking** — mark titles as `watched`, `pending`, or `dropped`
- **Filter & search** — query by genre, status, or rating range via query parameters
- **Auto docs** — interactive API documentation available at `/docs` (Swagger UI) and `/redoc`
- **Persistent storage** — SQLite database via SQLModel, no external DB setup needed

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/titles` | List all titles (supports filters) |
| `GET` | `/titles/{id}` | Get a single title by ID |
| `POST` | `/titles` | Add a new title |
| `PUT` | `/titles/{id}` | Update a title |
| `DELETE` | `/titles/{id}` | Delete a title |

### Project Structure

```
cinelog-api/
├── main.py           ← FastAPI app, route definitions
├── models.py         ← SQLModel table definitions
├── database.py       ← DB engine and session setup
├── schemas.py        ← Request and response schemas
├── requirements.txt
└── README.md
```

### Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API available at `http://localhost:8000` · Docs at `http://localhost:8000/docs`

### Example Request

```bash
curl -X POST http://localhost:8000/titles \
  -H "Content-Type: application/json" \
  -d '{"title": "Interstellar", "type": "movie", "genre": "sci-fi", "rating": 9, "status": "watched", "note": "Best third act in cinema."}'
```

### How it works

FastAPI reads the route definitions in `main.py` and automatically generates the OpenAPI schema. SQLModel ties Pydantic validation models directly to SQLAlchemy table definitions, so each title entry is validated on input and persisted to a local SQLite file. No migrations, no external database — just run and go.

### Tech

Python · FastAPI · SQLModel · SQLite · Uvicorn · Pydantic

---

## Español

API REST construida con FastAPI para registrar y calificar películas y series. Es como un Letterboxd personal mínimo — agrega títulos, escribe notas, asigna una calificación y márcalos como vistos o pendientes. Completamente documentada mediante la Swagger UI autogenerada en `/docs`.

### Características

- **CRUD completo** — crear, leer, actualizar y eliminar entradas de películas y series
- **Sistema de calificación** — puntúa cada título del 1 al 10 con una nota personal opcional
- **Seguimiento de estado** — marca títulos como `watched`, `pending` o `dropped`
- **Filtro y búsqueda** — consulta por género, estado o rango de calificación mediante query parameters
- **Documentación automática** — documentación interactiva disponible en `/docs` (Swagger UI) y `/redoc`
- **Almacenamiento persistente** — base de datos SQLite via SQLModel, sin configuración de DB externa

### Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/titles` | Lista todos los títulos (soporta filtros) |
| `GET` | `/titles/{id}` | Obtiene un título por ID |
| `POST` | `/titles` | Agrega un nuevo título |
| `PUT` | `/titles/{id}` | Actualiza un título |
| `DELETE` | `/titles/{id}` | Elimina un título |

### Estructura

```
cinelog-api/
├── main.py           ← App FastAPI, definición de rutas
├── models.py         ← Definición de tablas con SQLModel
├── database.py       ← Engine y sesión de base de datos
├── schemas.py        ← Esquemas de request y response
├── requirements.txt
└── README.md
```

### Ejecutar localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API disponible en `http://localhost:8000` · Docs en `http://localhost:8000/docs`

### Ejemplo de petición

```bash
curl -X POST http://localhost:8000/titles \
  -H "Content-Type: application/json" \
  -d '{"title": "Interstellar", "type": "movie", "genre": "sci-fi", "rating": 9, "status": "watched", "note": "Best third act in cinema."}'
```

### Cómo funciona

FastAPI lee las definiciones de rutas en `main.py` y genera automáticamente el esquema OpenAPI. SQLModel vincula directamente los modelos de validación de Pydantic con las definiciones de tabla de SQLAlchemy, por lo que cada entrada es validada al ingresar y persistida en un archivo SQLite local. Sin migraciones, sin base de datos externa — solo ejecuta y listo.

### Tecnologías

Python · FastAPI · SQLModel · SQLite · Uvicorn · Pydantic

---

<div align="center">
MIT License · Made by <a href="https://github.com/privatednicolas">privatednicolas</a>
</div>
