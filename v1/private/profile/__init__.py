from fastapi import APIRouter
from v1.private.profile.telegram import telegram_router

profile_router = APIRouter(prefix="/profile")

profile_router.include_router(profile_router)