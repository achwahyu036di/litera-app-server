from datetime import datetime
import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class payment(Base):
    __tabelname__ = "payment"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    payment_date = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    payment_status = Column(Enum('pending', 'success', 'failed', name='payment_status'))
    payment_amount = Column(Integer)
    payment_details = Column(Text)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    borrowing_id = Column(Integer, ForeignKey('borrowing.id'))
    user = relationship("user", back_populates="payment")

    