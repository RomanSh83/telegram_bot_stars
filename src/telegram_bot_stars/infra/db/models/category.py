from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from telegram_bot_stars.core.config import get_settings
from telegram_bot_stars.infra.db.models.base.base_model import BaseModel
from telegram_bot_stars.infra.db.models.mixins.model_mixins import (
    ByStampsMixin,
    TimestampsMixin,
    UIDMixin,
)

class Category(BaseModel, UIDMixin, TimestampsMixin, ByStampsMixin):
    title: Mapped[str] = mapped_column(String(get_settings().CATEGORY_TITLE_MAX_LENGTH), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text(), nullable=False)

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan", passive_deletes=True)

    def __repr__(self):
        return f"{self.title.title()}"
