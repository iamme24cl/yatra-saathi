from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserUpdate, UserResponse
from app.firebase_auth import verify_token_and_login
from app.services import user_service

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: UUID, updates: UserUpdate, current_user: User = Depends(verify_token_and_login), db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.firebase_uid != current_user.firebase_uid:
        raise HTTPException(status_code=403, detail="Not authorized")

    return user_service.update_user_info(user, updates, db)

@router.delete("/{user_id}")
def delete_user(user_id: UUID, current_user: User = Depends(verify_token_and_login), db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.firebase_uid != current_user.firebase_uid:
        raise HTTPException(status_code=403, detail="Not authorized")

    user_service.delete_user(user, db)
    return {"message": "User deleted successfully"}

