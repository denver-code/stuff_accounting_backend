from fastapi import APIRouter
from v1.schemas.user import UserSignUp
from v1.models.user import User

signup_router = APIRouter(prefix="/signup")

@signup_router.post("/")
async def signup_event(user: UserSignUp):
    user = user.dict()

    _user = User(email=user["email"], password=user["password"])

    await _user.insert()



    
