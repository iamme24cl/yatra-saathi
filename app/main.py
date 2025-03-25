from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "YatraSaathi API Running..."}
