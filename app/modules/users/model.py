from typing import TYPE_CHECKING

from alembic.environment import Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.providers.model import Provider


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(max_length=225, unique=True, index=True)
    password_hash: str = Field(max_length=225)
    is_active: bool = Field(default=True)
    provider: Optional["Provider"] = Relationship(
        back_populates="provider", sa_relationship_kwargs={"uselist": False}
    )
