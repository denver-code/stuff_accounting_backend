from fastapi import APIRouter, Depends

from app.core.tools.jwt import FastJWT
from v1.private.items import items_router
from v1.private.profile import profile_router

private_router = APIRouter(prefix="/private", dependencies=[
    Depends(
        FastJWT().login_required
        )
    ])

private_router.include_router(items_router)
private_router.include_router(profile_router)