from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    isbn = Column(String(32), unique=True, index=True)
    publisher = Column(String(255))
    year = Column(Integer)
    genres = Column(String(255))
    page_count = Column(Integer)
    format = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    ownership_records = relationship("Ownership", back_populates="book", cascade="all, delete-orphan")
    progress_records = relationship("ReadingProgress", back_populates="book", cascade="all, delete-orphan")

class Ownership(Base):
    __tablename__ = "ownership"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True)
    purchase_date = Column(Date)
    source = Column(String(255))
    condition = Column(String(100))
    location = Column(String(255))
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    book = relationship("Book", back_populates="ownership_records")

class ReadingProgress(Base):
    __tablename__ = "reading_progress"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True)
    start_date = Column(Date)
    last_update = Column(Date)
    current_page = Column(Integer)
    current_chapter = Column(String(255))
    status = Column(String(20), default="to-read")
    target_finish_date = Column(Date)
    finished_date = Column(Date)
    rating = Column(Integer)
    review = Column(Text)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("status IN ('to-read','reading','paused','finished')", name="chk_status"),
        CheckConstraint("rating BETWEEN 1 AND 5", name="chk_rating"),
    )

    book = relationship("Book", back_populates="progress_records")
