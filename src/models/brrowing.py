import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class Borrowing(Base):
    __tablename__ = "borrowing"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey("users.id"), nullable=False)
    book_id = Column(CHAR(36), ForeignKey("book.id"), nullable=False)
    borrow_date = Column(DateTime(timezone=True), nullable=False)
    return_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(String(50), default="dipinjam")  # "dipinjam", "selesai", "menunggu persetujuan", "dibatalkan", "ditolak"
    duration = Column(Integer, nullable=True)  # Duration in days

    user = relationship("User", back_populates="borrowings")
    book = relationship("Book", back_populates="borrowings")