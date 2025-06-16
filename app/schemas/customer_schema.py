from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class CustomerSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
