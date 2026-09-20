from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.categories.model import Category


class ServiceType(SQLModel, table=True):
    __tablename__ = "service_types"
    __table_args__ = (
        UniqueConstraint("category_id", "name", name="uq_service_types_category_name"),
    )
    id: int | None = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="categories.id", unique=True)
    name: str = Field(max_length=225)
    description: str | None = Field(default=None, max_length=500)
    category: "Category" = Relationship(back_populates="service_types")
