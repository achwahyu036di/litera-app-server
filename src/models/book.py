import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class User(Base):
    __tablename__ = "book"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey("user.user_id"))
    title = Column(String(255), nullable=False)
    writer = Column(String(255), nullable=False)
    publiser = Column(String(255))
    isbn = Column(String(13), unique=True, nullable=False)
    published_date = Column(DateTime(timezone=True), nullable=True)
    praice_per_day = Column(Integer, nullable=True)
    image_book_url = Column(String(2048), nullable=True)
    
    book_owner = relationship("User", back_populates="book")