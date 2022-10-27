from fastapi import APIRouter

from app.api.routes import symbols

api_router = APIRouter()
api_router.include_router(symbols.router, prefix="/symbols", tags=["symbols"])
