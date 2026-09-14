from sqlalchemy import table
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(max_length=225, unique=True, index=True)
    password_hash = Field(max_length=225)
    is_active: bool = Field(default=True)
