import uuid
from sqlalchemy import Column, String,Integer, DateTime, func
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy_imageattach import Image, image_attachment
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
    user_profile = image_attachment('UserPicture')

class UserPicture(Image):
    __tablename__ = 'user_pictures'
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), nullable=False)
    user = image_attachment(User, back_populates='user_profile')
    
    # def __repr__(self):
    #     return f"<UserPicture(id={self.id}, user_id={self.user_id})>"