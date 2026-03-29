from pydantic import BaseModel, Field, conint
from typing import Optional, List
from datetime import date, datetime

class OwnershipBase(BaseModel):
    purchase_date: Optional[date]
    source: Optional[str]
    condition: Optional[str]
    location: Optional[str]
    notes: Optional[str]

class OwnershipCreate(OwnershipBase):
    book_id: int

class OwnershipRead(OwnershipBase):
    id: int
    book_id: int

    class Config:
        from_attributes = True

class ReadingProgressBase(BaseModel):
    start_date: Optional[date]
    last_update: Optional[date]
    current_page: Optional[int]
    current_chapter: Optional[str]
    status: Optional[str] = Field(default="to-read")
    target_finish_date: Optional[date]
    finished_date: Optional[date]
    rating: Optional[conint(ge=1, le=5)]
    review: Optional[str]
    notes: Optional[str]

class ReadingProgressCreate(ReadingProgressBase):
    book_id: int

class ReadingProgressRead(ReadingProgressBase):
    id: int
    book_id: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str]
    publisher: Optional[str]
    year: Optional[int]
    genres: Optional[str]
    page_count: Optional[int]
    format: Optional[str]

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True

class BookWithDetails(BookRead):
    ownership_records: List[OwnershipRead] = []
    progress_records: List[ReadingProgressRead] = []
