import datetime
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverUpdate, DriverAvailabilityUpdate

def create_driver(driver_data: DriverCreate, user_id: UUID, db: Session) -> Driver:
    driver = Driver(**driver_data.model_dump(), user_id=user_id)
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver

def get_all_drivers(db: Session):
    return db.query(Driver).filter(Driver.available == True).all()

def get_driver_by_id(driver_id: UUID, db: Session) -> Driver | None:
    return db.query(Driver).filter(Driver.id == driver_id).first()

def update_driver(driver: Driver, updates: DriverUpdate, db: Session) -> Driver:
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(driver, field, value)
    db.commit()
    db.refresh(driver)
    return driver

def delete_driver(driver: Driver, db: Session):
    driver.deleted_at = datetime.utcnow()
    db.commit()
    db.refresh(driver)

def update_availability(driver: Driver, availability: DriverAvailabilityUpdate, db: Session) -> Driver:
    driver.available = availability.available
    db.commit()
    db.refresh(driver)
    return driver
