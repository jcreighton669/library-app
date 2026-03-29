from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from . import models, schemas
from datetime import date

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, updates: dict):
    db.query(models.Book).filter(models.Book.id == book_id).update(updates)
    db.commit()
    return get_book(db, book_id)

def delete_book(db: Session, book_id: int):
    db.query(models.Book).filter(models.Book.id == book_id).delete()
    db.commit()

def create_ownership(db: Session, ownership: schemas.OwnershipCreate):
    db_own = models.Ownership(**ownership.dict())
    db.add(db_own)
    db.commit()
    db.refresh(db_own)
    return db_own

def get_ownership_for_book(db: Session, book_id: int):
    return db.query(models.Ownership).filter(models.Ownership.book_id == book_id).all()

def create_progress(db: Session, progress: schemas.ReadingProgressCreate):
    db_progress = models.ReadingProgress(**progress.dict())
    if db_progress.last_update is None:
        db_progress.last_update = date.today()
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress

def get_progress_for_book(db: Session, book_id: int):
    return db.query(models.ReadingProgress).filter(models.ReadingProgress.book_id == book_id).all()

def update_progress(db: Session, progress_id: int, updates: dict):
    if "last_update" not in updates:
        updates["last_update"] = date.today()
    db.query(models.ReadingProgress).filter(models.ReadingProgress.id == progress_id).update(updates)
    db.commit()
    return db.query(models.ReadingProgress).filter(models.ReadingProgress.id == progress_id).first()

def delete_progress(db: Session, progress_id: int):
    db.query(models.ReadingProgress).filter(models.ReadingProgress.id == progress_id).delete()
    db.commit()
