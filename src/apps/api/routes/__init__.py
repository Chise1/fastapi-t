from fastapi import APIRouter

from . import t1

api_router = APIRouter(prefix="/api")
api_router.include_router(t1.router)
