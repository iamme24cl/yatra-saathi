from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    driver_id = Column(UUID(as_uuid=True), ForeignKey("drivers.id"), nullable=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=True)
    
    type = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    passenger_capacity = Column(Integer)
    license_number = Column(String, unique=True)
    
    available = Column(Boolean, default=True)

    driver = relationship("Driver", back_populates="vehicle")
    company = relationship("Company", back_populates="vehicles")
