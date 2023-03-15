from fastapi import APIRouter, HTTPException
from app.core.tools.jwt import FastJWT
from v1.schemas.user import User as UserSchema
from app.core.tools.database import find_one

signin_router = APIRouter(prefix="/signin")

@signin_router.post("/")
async def signin_event(user: UserSchema):
    _user = await find_one("users_db", {"email": user.email})

    if not _user:
        raise HTTPException(401, "Email or password are incorect!")

    if user.password != _user["password"]:
        raise HTTPException(401, "Email or password are incorect!")

    jwt_token = await FastJWT().encode(optional_data={
        "email": user.email
    })

    return {"token": jwt_token}