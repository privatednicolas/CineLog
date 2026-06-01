from typing import Optional
from sqlmodel import Field, SQLModel


class TitleBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    type: str = Field(description="'movie' or 'series'")
    genre: Optional[str] = Field(default=None, max_length=100)
    year: Optional[int] = Field(default=None, ge=1888, le=2100)
    rating: Optional[float] = Field(default=None, ge=1.0, le=10.0)
    status: str = Field(
        default="pending",
        description="'watched', 'pending', or 'dropped'"
    )
    note: Optional[str] = Field(default=None, max_length=1000)


class Title(TitleBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TitleCreate(TitleBase):
    pass


class TitleUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    type: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = Field(default=None, ge=1888, le=2100)
    rating: Optional[float] = Field(default=None, ge=1.0, le=10.0)
    status: Optional[str] = None
    note: Optional[str] = None


class TitleRead(TitleBase):
    id: int
