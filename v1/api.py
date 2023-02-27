from fastapi import APIRouter
from v1.private import private_router
from v1.public import public_router

v1_router = APIRouter(prefix="/api/v1")

@v1_router.get("/")
async def showcase_event():
    return {
        "message": "Welcome on 1'st version of our server, stranger!",
    }

v1_router.include_router(private_router)
v1_router.include_router(public_router)