from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
import os

from database import create_db, get_session
from models import Title, TitleCreate, TitleRead, TitleUpdate

app = FastAPI(
    title="cinelog-api",
    description=(
        "Personal movie & series tracker. "
        "Log titles, rate them, write notes, and track your watch status."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def serve_ui():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(html_path)


@app.on_event("startup")
def on_startup():
    create_db()


# ── GET /titles ──────────────────────────────────────────────────────────────

@app.get("/titles", response_model=list[TitleRead], tags=["Titles"])
def list_titles(
    status: Optional[str] = Query(default=None, description="Filter by status: watched, pending, dropped"),
    type: Optional[str] = Query(default=None, description="Filter by type: movie, series"),
    genre: Optional[str] = Query(default=None, description="Filter by genre (partial match)"),
    min_rating: Optional[float] = Query(default=None, ge=1, le=10),
    max_rating: Optional[float] = Query(default=None, ge=1, le=10),
    session: Session = Depends(get_session),
):
    """List all titles. Supports filtering by status, type, genre, and rating range."""
    query = select(Title)

    if status:
        query = query.where(Title.status == status)
    if type:
        query = query.where(Title.type == type)
    if genre:
        query = query.where(Title.genre.ilike(f"%{genre}%"))
    if min_rating is not None:
        query = query.where(Title.rating >= min_rating)
    if max_rating is not None:
        query = query.where(Title.rating <= max_rating)

    return session.exec(query).all()


# ── GET /titles/{id} ─────────────────────────────────────────────────────────

@app.get("/titles/{title_id}", response_model=TitleRead, tags=["Titles"])
def get_title(title_id: int, session: Session = Depends(get_session)):
    """Get a single title by its ID."""
    title = session.get(Title, title_id)
    if not title:
        raise HTTPException(status_code=404, detail="Title not found")
    return title


# ── POST /titles ─────────────────────────────────────────────────────────────

@app.post("/titles", response_model=TitleRead, status_code=201, tags=["Titles"])
def create_title(data: TitleCreate, session: Session = Depends(get_session)):
    """Add a new movie or series to your log."""
    valid_types = {"movie", "series"}
    valid_statuses = {"watched", "pending", "dropped"}

    if data.type not in valid_types:
        raise HTTPException(status_code=422, detail=f"type must be one of: {valid_types}")
    if data.status not in valid_statuses:
        raise HTTPException(status_code=422, detail=f"status must be one of: {valid_statuses}")

    title = Title.model_validate(data)
    session.add(title)
    session.commit()
    session.refresh(title)
    return title


# ── PUT /titles/{id} ─────────────────────────────────────────────────────────

@app.put("/titles/{title_id}", response_model=TitleRead, tags=["Titles"])
def update_title(
    title_id: int,
    data: TitleUpdate,
    session: Session = Depends(get_session),
):
    """Update any field of an existing title. Only send fields you want to change."""
    title = session.get(Title, title_id)
    if not title:
        raise HTTPException(status_code=404, detail="Title not found")

    update_data = data.model_dump(exclude_unset=True)

    if "type" in update_data and update_data["type"] not in {"movie", "series"}:
        raise HTTPException(status_code=422, detail="type must be 'movie' or 'series'")
    if "status" in update_data and update_data["status"] not in {"watched", "pending", "dropped"}:
        raise HTTPException(status_code=422, detail="status must be 'watched', 'pending', or 'dropped'")

    for key, value in update_data.items():
        setattr(title, key, value)

    session.add(title)
    session.commit()
    session.refresh(title)
    return title


# ── DELETE /titles/{id} ──────────────────────────────────────────────────────

@app.delete("/titles/{title_id}", status_code=204, tags=["Titles"])
def delete_title(title_id: int, session: Session = Depends(get_session)):
    """Delete a title from your log."""
    title = session.get(Title, title_id)
    if not title:
        raise HTTPException(status_code=404, detail="Title not found")
    session.delete(title)
    session.commit()


# ── GET /stats ────────────────────────────────────────────────────────────────

@app.get("/stats", tags=["Stats"])
def get_stats(session: Session = Depends(get_session)):
    """Quick summary of your log: counts by status, type, and top-rated titles."""
    all_titles = session.exec(select(Title)).all()

    if not all_titles:
        return {"total": 0, "message": "No titles logged yet."}

    watched = [t for t in all_titles if t.status == "watched"]
    pending = [t for t in all_titles if t.status == "pending"]
    dropped = [t for t in all_titles if t.status == "dropped"]
    rated = [t for t in all_titles if t.rating is not None]

    top_rated = sorted(rated, key=lambda t: t.rating, reverse=True)[:5]

    return {
        "total": len(all_titles),
        "by_status": {
            "watched": len(watched),
            "pending": len(pending),
            "dropped": len(dropped),
        },
        "by_type": {
            "movies": len([t for t in all_titles if t.type == "movie"]),
            "series": len([t for t in all_titles if t.type == "series"]),
        },
        "average_rating": (
            round(sum(t.rating for t in rated) / len(rated), 2) if rated else None
        ),
        "top_rated": [
            {"id": t.id, "title": t.title, "rating": t.rating}
            for t in top_rated
        ],
    }
