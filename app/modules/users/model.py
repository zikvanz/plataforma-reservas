from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import CheckConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.providers.model import Provider
    from app.modules.bookings.model import Booking


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'provider', 'client')", name="ck_users_role"
        ),
    )
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(max_length=225, unique=True, index=True)
    password_hash: str = Field(max_length=225)
    is_active: bool = Field(default=True)
    role: str = Field(
        default="client",
        max_length=20,
        index=True,
        sa_column_kwargs={"server_default": "client"},
    )
    provider: Optional["Provider"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"uselist": False}
    )
    bookings: List["Booking"] = Relationship(back_populates="client")
