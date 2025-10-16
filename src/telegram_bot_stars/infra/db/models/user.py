from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from telegram_bot_stars.infra.db.models.base.base_model import BaseModel
from telegram_bot_stars.infra.db.models.mixins.model_mixins import CreateMixin


class User(BaseModel, CreateMixin):
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
