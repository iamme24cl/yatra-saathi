from fastapi import APIRouter, Depends
from app.firebase_auth import verify_firebase_token
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/verify", response_model=UserResponse)
def verify_user(user=Depends(verify_firebase_token)):
    return user