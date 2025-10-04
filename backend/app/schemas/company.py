from pydantic import BaseModel
from datetime import datetime

class CompanyCreate(BaseModel):
    name: str
    country: str

class CompanyResponse(BaseModel):
    id: int
    name: str
    country: str
    currency: str
    created_at: datetime

    class Config:
        from_attributes = True
