import datetime
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleUpdate

def create_vehicle(vehicle_data: VehicleCreate, db: Session) -> Vehicle:
    vehicle = Vehicle(**vehicle_data.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_vehicle_by_id(vehicle_id: UUID, db: Session) -> Vehicle | None:
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

def update_vehicle(vehicle: Vehicle, updates: VehicleUpdate, db: Session) -> Vehicle:
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(vehicle, field, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def delete_vehicle(vehicle: Vehicle, db: Session):
    vehicle.deleted_at = datetime.datetime.now(datetime.timezone.utc)
    db.commit()
    db.refresh(vehicle)
