from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime

from app.models.booking import Booking
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingUpdate


def create_booking(db: Session, user: User, booking_data: BookingCreate):
    booking = Booking(
        user_id=user.id,
        pickup_location=booking_data.pickup_location,
        dropoff_location=booking_data.dropoff_location,
        scheduled_time=booking_data.scheduled_time
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def get_all_bookings(db: Session, user: User):
    return db.query(Booking).filter(Booking.user_id == user.id).all()


def get_booking_by_id(db: Session, booking_id: UUID, user: User):
    return db.query(Booking).filter(
        Booking.id == booking_id, Booking.user_id == user.id
    ).first()


def update_booking(db: Session, booking_id: UUID, update_data: BookingUpdate, user: User):
    booking = get_booking_by_id(db, booking_id, user)
    if not booking:
        raise ValueError("Booking not found")

    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(booking, key, value)

    db.commit()
    db.refresh(booking)
    return booking


def cancel_booking(db: Session, booking_id: UUID, user: User):
    booking = get_booking_by_id(db, booking_id, user)
    if not booking:
        raise ValueError("Booking not found")

    booking.cancelled_at = datetime.now(datetime.timezone.utc)
    db.commit()
