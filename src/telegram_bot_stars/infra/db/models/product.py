from uuid import UUID

from sqlalchemy import Float, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from telegram_bot_stars.core.config import get_settings
from telegram_bot_stars.infra.db.models.base.base_model import BaseModel
from telegram_bot_stars.infra.db.models.mixins.model_mixins import (
    ByStampsMixin,
    TimestampsMixin,
    UIDMixin,
)


class Product(BaseModel, UIDMixin, TimestampsMixin, ByStampsMixin):
    name: Mapped[str] = mapped_column(String(get_settings().PRODUCT_NAME_MAX_LENGTH), nullable=False)
    category_uid: Mapped[UUID] = mapped_column(
        ForeignKey("category.uid", name="fk_product_category_uid"), nullable=False
    )
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    image: Mapped[str] = mapped_column(String(64), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    category = relationship("Category", back_populates="products")

    __table_args__ = (UniqueConstraint("name", "category_uid"),)

    def __repr__(self):
        return f"{self.name.title()}"
