from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.dependencies import get_current_user
from app.database import get_db
from app.models.user import User 
from app.schemas.driver import DriverCreate, DriverUpdate, DriverAvailabilityUpdate, DriverResponse
from app.services import driver_service

router = APIRouter()

@router.post("/", response_model=DriverResponse)
def register_driver(driver_data: DriverCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return driver_service.create_driver(driver_data, current_user.id, db)

@router.get("/", response_model=list[DriverResponse])
def get_available_drivers(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return driver_service.get_all_drivers(db)

@router.get("/{driver_id}", response_model=DriverResponse)
def get_driver(driver_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    driver = driver_service.get_driver_by_id(driver_id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.put("/{driver_id}", response_model=DriverResponse)
def update_driver(driver_id: UUID, updates: DriverUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    driver = driver_service.get_driver_by_id(driver_id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver_service.update_driver(driver, updates, db)

@router.delete("/{driver_id}")
def delete_driver(driver_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    driver = driver_service.get_driver_by_id(driver_id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    driver_service.delete_driver(driver, db)
    return {"message": "Driver deleted successfully"}

@router.patch("/{driver_id}/availability", response_model=DriverResponse)
def update_driver_availability(driver_id: UUID, availability: DriverAvailabilityUpdate, db: Session = Depends(get_db), current_user: User = Depends(verify_token_and_login)):
    driver = driver_service.get_driver_by_id(driver_id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver_service.update_availability(driver, availability, db)
