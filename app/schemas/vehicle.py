from pydantic import BaseModel
from uuid import UUID
from typing import Optional

from app.schemas.company import CompanyResponse

class VehicleBase(BaseModel):
    type: str
    model: str
    year: int
    passenger_capacity: int
    license_number: str

class VehicleCreate(VehicleBase):
    company_id: Optional[UUID] = None  # Optional if it's a personal vehicle
    driver_id: Optional[UUID] = None # Optional if it's a company vehicle
    
class VehicleUpdate(VehicleBase):
    company_id: Optional[UUID] = None  # Optional if it's a personal vehicle
    driver_id: Optional[UUID] = None # Optional if it's a company vehicle

class VehicleResponse(VehicleBase):
    id: UUID
    company_id: Optional[UUID] = None
    company: Optional[CompanyResponse] = None
    driver_id: Optional[UUID] = None

    class Config:
        orm_mode = True