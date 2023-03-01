import re
from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str
    picture: str
    tag: Optional[str] = "Other"


class ItemUPC(BaseModel):
    ucp: int
    tag: Optional[str] = "Other"