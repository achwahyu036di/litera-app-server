from pydantic import BaseModel, EmailStr, ConfigDict, HttpUrl
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    nik: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    address: Optional[str] = None
    telephone: Optional[str] = None
    created_at: Optional[datetime] = None
    profile_image_url: Optional[HttpUrl] = None

    # set orm
    model_config = ConfigDict(from_attributes=True)