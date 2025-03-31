from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.firebase_auth import verify_token_and_login
from app.models.user import User

def get_current_user(user: User = Depends(verify_token_and_login)) -> User:
  return user 

def get_current_admin(current_user: User = Depends(get_current_user)) -> User: 
  if current_user.role != "admin":
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="You do not have permission to perform this action."
    )
  return current_user