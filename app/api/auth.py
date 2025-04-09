from fastapi import APIRouter, Depends
from app.firebase_auth import verify_token_and_register, verify_token_and_login
from app.schemas.user import UserResponse

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user=Depends(verify_token_and_register)):
    return user

@router.post("/login", response_model=UserResponse)
def login_user(user=Depends(verify_token_and_login)):
    return user

