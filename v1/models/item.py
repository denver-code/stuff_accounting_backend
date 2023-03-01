from fastapi import HTTPException
from typing import Optional
from pydantic import BaseModel
from app.core.tools.database import insert_one, is_user_exist

class Item(BaseModel):
    title: str
    description: str
    picture: str
    tag: Optional[str] = "Other"
    upc: Optional[str]
    owner: str

    async def insert(self):
        item_dict = self.dict()
        return await insert_one("items_db", item_dict)
