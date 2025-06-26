from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import Optional, Literal
from datetime import datetime

class BookSchema(BaseModel):
    id_user: Optional[str] = None
    tittle: Optional[str] = None
    writer: Optional[str] = None
    publiser = Optional[str] = None
    status: Literal["tersedia", "dipinjam", "rusak", "hilang"] = "tersedia"
    duration = Optional[int] = None
    user_rules = Optional[str] = None
    create_at = Optional[datetime]
    profile_image_url: Optional[HttpUrl] = None

    model_config = ConfigDict(from_attributes=True)