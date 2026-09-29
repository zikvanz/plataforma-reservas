# import time
from datetime import time
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.providers.model import Provider


class AvailabilityRule(SQLModel, table=True):
    __tablename__ = "availability_rules"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "day_of_week",
            "start_time",
            "end_time",
            name="uq_availability_rules_provider_date_time",
        ),
        CheckConstraint(
            "day_of_week BETWEEN 0 AND 6", name="ck_availability_rules_valid_day"
        ),
        CheckConstraint(
            "start_time < end_time", name="ck_availability_rules_valid_time_range"
        ),
    )
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    day_of_week: int
    start_time: time
    end_time: time
    is_active: bool = Field(default=True)
    provider: "Provider" = Relationship(back_populates="availability_rules")
