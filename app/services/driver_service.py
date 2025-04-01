import datetime
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleInfo
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverUpdate, DriverAvailabilityUpdate
from app.models.user import User 

def create_driver(driver_data: DriverCreate, user: User, db: Session) -> Driver:
    driver = Driver(**driver_data.model_dump(), user_id=user.id)
    db.add(driver)
    db.flush() # This gives the driver and ID before vehicle creation
    
    if user.role == "driver" and driver.company_id is None and driver_data.vehicle_info:
        # Create associated vehicle
        vehicle_info: VehicleInfo = driver_data.vehicle_info
        vehicle = Vehicle(**vehicle_info.model_dump(), driver_id=driver.id)
        db.add(vehicle)
    
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
