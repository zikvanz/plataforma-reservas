from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.modules.provider_services.model import ProviderService

if TYPE_CHECKING:
    from app.modules.users.model import User


class Provider(SQLModel, table=True):
    __tablename__ = "providers"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", unique=True)
    bussiness_name: str = Field(max_length=225)
    description: str | None = Field(default=None, max_length=500)
    direction: str = Field(max_length=300)
    is_verified: bool = Field(default=False)
    user: "User" = Relationship(back_populates="user")
    provider_service: list["ProviderService"] = Relationship(back_populates="providers")
