from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class VehicleInfo(BaseModel):
    type: str
    model: str
    year: int
    passenger_capacity: int
    license_number: str

class DriverCreate(BaseModel):
    vehicle_info: VehicleInfo

class DriverUpdate(BaseModel):
    vehicle_info: VehicleInfo

class DriverAvailabilityUpdate(BaseModel):
    available: bool

class DriverResponse(BaseModel):
    id: UUID
    vehicle_info: VehicleInfo
    available: bool

    class Config:
        orm_mode = True
