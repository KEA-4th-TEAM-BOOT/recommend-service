from fastapi import APIRouter
from api.routes import upsert, get

api_router = APIRouter()

api_router.include_router(upsert.router, prefix="/upsert", tags=["upsert"])
api_router.include_router(get.router, prefix="/get", tags=["get"])