from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from app.schemas.company import CompanyResponse
from app.schemas.vehicle import VehicleResponse, VehicleCreate  

class DriverCreate(BaseModel):
    vehicle_id: UUID
    vehicle_info:  VehicleCreate 

class DriverUpdate(BaseModel):
    available: Optional[bool] = None
    company_id: Optional[UUID] = None
    vehicle_id: Optional[UUID] = None

class DriverAvailabilityUpdate(BaseModel):
    available: bool

class DriverResponse(BaseModel):
    id: UUID
    available: bool
    company_id: Optional[UUID] = None
    vehicle: Optional[VehicleResponse] = None  
    company: Optional[CompanyResponse] = None
    
    class Config:
        orm_mode = True
