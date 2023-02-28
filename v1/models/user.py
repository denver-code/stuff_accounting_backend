from fastapi import HTTPException
from typing import Optional
from pydantic import BaseModel
from app.core.tools.database import insert_one, is_user_exist

class User(BaseModel):
    email: str
    password: str
    saved: Optional[list] = []
    telegram_id: Optional[int]
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False

    async def insert(self):
        user_dict = self.dict()
        if await is_user_exist(self.email):
            raise HTTPException(409, "User already exist.")
        return await insert_one("users_db", user_dict)