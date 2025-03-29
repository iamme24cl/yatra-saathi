from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, user, driver

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(driver.router, prefix="/drivers", tags=["Drivers"])

@app.get("/")
def root():
    return {"message": "YatraSaathi API Running..."}
