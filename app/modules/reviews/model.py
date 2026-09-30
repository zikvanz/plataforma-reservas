from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Column, DateTime
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.bookings.model import Booking


class Review(SQLModel, table=True):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5", name="ck_reviews_valid_rating"),
    )
    id: int | None = Field(default=None, primary_key=True)
    booking_id: int = Field(foreign_key="bookings.id", unique=True)
    rating: int
    comment: str | None = Field(default=None, max_length=500)
    create_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        ),
    )
    booking: "Booking" = Relationship(back_populates="review")
