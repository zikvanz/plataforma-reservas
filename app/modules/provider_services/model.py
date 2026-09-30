from decimal import Decimal
from typing import TYPE_CHECKING, List

from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.service_catalog.model import ServiceType
    from app.modules.providers.model import Provider
    from app.modules.bookings.model import Booking


class ProviderService(SQLModel, table=True):
    __tablename__ = "provider_services"
    __table_args__ = (
        UniqueConstraint(
            "provider_id",
            "service_type_id",
            name="uq_provider_services_provider_service_type",
        ),
        CheckConstraint("price > 0", name="ck_provider_services_price_positive"),
        CheckConstraint("duration_minutes > 0", name="ck_provider_services_duration_positive"),
    )

    id: int | None = Field(default=None, primary_key=True)
    provider_id: int = Field(foreign_key="providers.id", index=True)
    service_type_id: int = Field(foreign_key="service_types.id", index=True)
    price: Decimal = Field(max_digits=10, decimal_places=2)
    duration_minutes: int
    description: str | None = Field(default=None, max_length=500)
    is_active: bool = Field(default=True)
    provider: "Provider" = Relationship(back_populates="provider_services")
    service_type: "ServiceType" = Relationship(back_populates="provider_services")
    bookings: List["Booking"] = Relationship(back_populates="provider_service")
