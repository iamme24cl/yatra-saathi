from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, unique=True, nullable=False)
    contact_email = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)

    drivers = relationship("Driver", back_populates="company")
    vehicles = relationship("Vehicle", back_populates="company")