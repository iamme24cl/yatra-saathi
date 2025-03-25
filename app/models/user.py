import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    firebase_uid = Column(String, unique=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, default="customer") # driver, customer, admin
