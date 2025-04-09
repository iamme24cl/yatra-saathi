from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingUpdate, BookingResponse
from app.services import booking_service
from app.dependencies import get_current_user, get_current_admin

router = APIRouter()

@router.post("/", response_model=BookingResponse)
def create_new_booking(
    booking_data: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return booking_service.create_booking(db, current_user, booking_data)

@router.get("/", response_model=list[BookingResponse])
def get_bookings(
    db: Session = Depends(get_db),
    admin_user: User = Depends(get_current_admin)
):
    return booking_service.get_all_bookings(db, admin_user)

@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    booking = booking_service.get_booking_by_id(db, booking_id, current_user)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.put("/{booking_id}", response_model=BookingResponse)
def update_booking_details(
    booking_id: UUID,
    update_data: BookingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return booking_service.update_booking(db, booking_id, update_data, current_user)

@router.delete("/{booking_id}")
def cancel_existing_booking(
    booking_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    booking_service.cancel_booking(db, booking_id, current_user)
    return {"message": "Booking canceled successfully"}
