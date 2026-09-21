from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.service_types.model import ServiceType
    from app.modules.providers.model import Provider


class ProviderService(SQLModel, table=True):
    __tablename__ = "provider_services"
    id: int | None = Field(default=None, primary_key=True)
    provider_id: int = Field(foreign_key="providers.id", index=True)
    service_type_id: int = Field(foreign_key="service_types.id", index=True)
    # name: str = Field(max_length=225, unique=True)
    price: Decimal = Field(max_digits=10, decimal_places=2)
    duration_minutes: int
    description: str | None = Field(default=None, max_length=500)
    is_active: bool = Field(default=True)
    provider: "Provider" = Relationship(back_populates="provider_services")
    service_type: "ServiceType" = Relationship(back_populates="provider_services")
