from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class DriverCreate(BaseModel):
    name: str
    phone: str
    vehicle_info: Optional[str] = None

class DriverUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    vehicle_info: Optional[str]

class DriverAvailabilityUpdate(BaseModel):
    available: bool

class DriverResponse(BaseModel):
    id: UUID
    name: str
    phone: str
    vehicle_info: Optional[str]
    available: bool

    class Config:
        orm_mode = True
