from fastapi import APIRouter
from app.core.tools.jwt import FastJWT
from v1.schemas.user import User as UserSchema
from v1.models.user import User as UserModel

signup_router = APIRouter(prefix="/signup")

@signup_router.post("/")
async def signup_event(user: UserSchema):
    user = user.dict()

    _user = UserModel(email=user["email"], password=user["password"])

    await _user.insert()

    jwt_token = await FastJWT().encode(optional_data={
        "email": user["email"]
    })

    return {"message": "User created!", "token": jwt_token}