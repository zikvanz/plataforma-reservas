from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.service_types.model import ServiceType


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=225, unique=True)
    description: str | None = Field(default=None, max_length=500)
    is_active: bool = Field(default=True)
    service_types: list["ServiceType"] = Relationship(back_populates="provider")
