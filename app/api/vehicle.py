from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse
from app.services import vehicle_service
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=VehicleResponse)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # Vehicle must be tied to a driver account
    if not user.driver:
        raise HTTPException(status_code=403, detail="Only drivers can create vehicles")
    return vehicle_service.create_vehicle(vehicle, user.driver.id, db)

@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: UUID, db: Session = Depends(get_db)):
    vehicle = vehicle_service.get_vehicle_by_id(vehicle_id, db)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(vehicle_id: UUID, updates: VehicleUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    vehicle = vehicle_service.get_vehicle_by_id(vehicle_id, db)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle_service.update_vehicle(vehicle, updates, db)

@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    vehicle = vehicle_service.get_vehicle_by_id(vehicle_id, db)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle_service.delete_vehicle(vehicle, db)
    return {"message": "Vehicle deleted successfully"}
