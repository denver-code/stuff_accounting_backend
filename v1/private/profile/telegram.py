from fastapi import APIRouter, Request
from app.core.tools.database import find_one, update_one 

from app.core.tools.jwt import FastJWT

telegram_router = APIRouter(prefix="/telegram")

@telegram_router.post("/set")
async def get_profile_items_event(request: Request, telegram_id: str):
    auth_token = request.headers["Authorisation"]
    auth_token = await FastJWT().decode(auth_token)
    user = await find_one("users_db", {"email": auth_token["email"]})

    user["telegram"] = telegram_id
    await update_one("users_db", {"email": auth_token["email"]}, user)

    return {"message": "Updated."}