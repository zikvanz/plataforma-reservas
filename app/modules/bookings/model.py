from datetime import datetime, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from sqlalchemy import CheckConstraint, Column, DateTime, Index
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.provider_services.model import ProviderService
    from app.modules.users.model import User
    from app.modules.reviews.model import Review


class Booking(SQLModel, table=True):
    __tablename__ = "bookings"
    __table_args__ = (
        CheckConstraint("start_at < end_at", name="ck_bookings_valid_time_range"),
        CheckConstraint("0 < price_at_booking", name="ck_bookings_price_positive"),
        CheckConstraint(
            "status IN ('pending', 'confirmed', 'completed','canceled')",
            name="ck_bookings_valid_status",
        ),
        Index(
            "ix_bookings_client_start",
            "client_id",
            "start_at",
        ),
        Index(
            "ix_bookings_provider_service_start",
            "provider_service_id",
            "start_at",
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="users.id")
    provider_service_id: int = Field(foreign_key="provider_services.id")
    start_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        )
    )
    end_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        )
    )
    price_at_booking: Decimal = Field(max_digits=10, decimal_places=2)
    status: str = Field(default="pending", max_length=20)
    notes: str | None = Field(default=None, max_length=1000)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        ),
    )
    client: "User" = Relationship(back_populates="bookings")
    provider_service: "ProviderService" = Relationship(back_populates="bookings")
    review: Optional["Review"] = Relationship(back_populates="booking")
