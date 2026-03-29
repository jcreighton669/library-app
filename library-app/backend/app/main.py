from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI(title="Library Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

@app.get("/books", response_model=list[schemas.BookRead])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=schemas.BookWithDetails)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.post("/books", response_model=schemas.BookRead, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book=book)

@app.patch("/books/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book: schemas.BookBase, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db, book_id, book.dict(exclude_unset=True))

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, book_id)
    return None

@app.post("/books/{book_id}/ownership", response_model=schemas.OwnershipRead, status_code=201)
def add_ownership(book_id: int, ownership: schemas.OwnershipBase, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    ownership_data = schemas.OwnershipCreate(book_id=book_id, **ownership.dict(exclude_unset=True))
    return crud.create_ownership(db, ownership=ownership_data)

@app.get("/books/{book_id}/ownership", response_model=list[schemas.OwnershipRead])
def get_ownership(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.get_ownership_for_book(db, book_id)

@app.post("/books/{book_id}/progress", response_model=schemas.ReadingProgressRead, status_code=201)
def add_progress(book_id: int, progress: schemas.ReadingProgressBase, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    progress_data = schemas.ReadingProgressCreate(book_id=book_id, **progress.dict(exclude_unset=True))
    return crud.create_progress(db, progress=progress_data)

@app.get("/books/{book_id}/progress", response_model=list[schemas.ReadingProgressRead])
def get_progress(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.get_progress_for_book(db, book_id)

@app.patch("/progress/{progress_id}", response_model=schemas.ReadingProgressRead)
def update_reading_progress(progress_id: int, progress: schemas.ReadingProgressBase, db: Session = Depends(get_db)):
    updated = crud.update_progress(db, progress_id, progress.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Progress record not found")
    return updated

@app.delete("/progress/{progress_id}", status_code=204)
def delete_reading_progress(progress_id: int, db: Session = Depends(get_db)):
    crud.delete_progress(db, progress_id)
    return None
