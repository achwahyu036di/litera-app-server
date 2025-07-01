from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class BorrowingSchema(BaseModel):
    id_user: Optional[str] = None
    id_book: Optional[str] = None
    duration: Optional[int] = None  # Duration in days
    user_rules: Optional[str] = None
    borrow_date: Optional[datetime] = None
    return_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)