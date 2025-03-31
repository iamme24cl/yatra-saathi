from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.api.user import router as user_router
from app.api.driver import router as driver_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])
api_router.include_router(driver_router, prefix="/drivers", tags=["Drivers"])
