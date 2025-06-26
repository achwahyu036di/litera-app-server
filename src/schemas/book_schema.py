from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import Optional, Literal
from datetime import datetime

class BookSchema(BaseModel):
    id_user: Optional[str] = None
    tittle: Optional[str] = None
    writer: Optional[str] = None
    publiser = Optional[str] = None
    isbn: Optional[str] = None
    published_date: Optional[datetime] = None
    price_per_day: Optional[int] = None
    image_book_url: Optional[HttpUrl] = None

    model_config = ConfigDict(from_attributes=True)