import re
from pydantic import BaseModel, validator

from app.core.tools.email_fixer import EmailFixer

class User(BaseModel):
    email: str
    password: str

    @validator("email")
    def check_email_event(cls, v):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, v):
            raise ValueError("Invalid email")
        v = EmailFixer.fix(v)
        return v

    @validator('password')
    def validate_sha256(cls, v):
        pattern = re.compile(r'^[0-9a-fA-F]{64}$')
        if not bool(pattern.match(v)):
            raise ValueError('Invalid SHA-256 hash')
        return v