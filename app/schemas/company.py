from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: UUID

    class Config:
        orm_mode = True
