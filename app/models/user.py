import uuid
from sqlalchemy import Column, String,Integer, DateTime, func
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nik = Column(CHAR(36), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False, unique=True)
    address = Column(String(255), nullable=True)
    telephone = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
