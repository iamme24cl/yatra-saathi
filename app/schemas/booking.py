from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BookingCreate(BaseModel):
    driver_id: UUID
    pickup_location: str
    dropoff_location: str
    scheduled_time: datetime

class BookingUpdate(BaseModel):
    pickup_location: Optional[str] = None
    dropoff_location: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    status: Optional[str] = None

class BookingResponse(BaseModel):
    id: UUID
    user_id: UUID
    driver_id: UUID
    pickup_location: str
    dropoff_location: str
    scheduled_time: datetime
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    cancelled_at: Optional[datetime] = None

    class Config:
        orm_mode = True
