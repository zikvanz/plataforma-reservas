from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr
from sqlmodel import Field

UserRole = Literal["admin", "provider", "client"]

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(max_length=250)
    password: str = Field(min_length=8, max_length=150)
    model_config = ConfigDict(extra="forbid")


class UserRead(BaseModel):
    name: str
    email: EmailStr
    is_active: bool
    role: UserRole
    model_config = ConfigDict(from_attributes=True)
