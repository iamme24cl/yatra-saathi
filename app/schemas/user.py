import uuid
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserUpdate(BaseModel):
  email: Optional[EmailStr]
  name: Optional[str]
  phone: Optional[str]
  
class UserResponse(BaseModel):
  id: uuid.UUID
  firebase_uid: str 
  email: Optional[EmailStr] = None 
  name: Optional[str] = None
  phone: Optional[str] = None
  role: Optional[str] = None
  
  class Config:
    orm_mode = True # This enables SQLALchemy model -> Pydantic conversion
  