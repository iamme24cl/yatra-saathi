from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)

    vehicle_info = Column(
        JSON,
        nullable=True,
        comment="Vehicle info as JSON: type, model, year, passenger_capacity, license_number"
    )
    available = Column(Boolean, default=True)

    user = relationship("User", back_populates="driver")
