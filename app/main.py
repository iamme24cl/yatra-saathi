import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logger import logging
from app.api.routes import api_router

logger = logging.getLogger(__name__)
logger.info("Starting YatraSaathi backend...")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def root():
    logger.info("Root route accessed")
    return {"message": "YatraSaathi API Running..."}
