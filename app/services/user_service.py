import datetime
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.user import User
from app.schemas.user import UserUpdate

def get_user_by_id(user_id: UUID, db: Session) -> User | None:
  return db.query(User).filter(User.id == user_id).first()

def update_user_info(user: User, updates: UserUpdate, db: Session) -> User:
  user.email = updates.email or user.email
  user.name = updates.name or user.name
  user.phone = updates.phone or user.phone
  db.commit()
  db.refresh(user)
  return user

def delete_user(user: User, db: Session):
  user.deleted_at = datetime.utcnow()
  db.commit()
  db.refresh(user)
  
  
  