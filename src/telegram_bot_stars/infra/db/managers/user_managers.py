from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

from telegram_bot_stars.bot_logic.schemas.user_schemas import UserSchema
from telegram_bot_stars.core.base.singleton import Singleton
from telegram_bot_stars.infra.db.adapter.postgre_adapter import (
    PostgresAdapter,
    get_db_adapter,
)
from telegram_bot_stars.infra.db.models.user import User as DBUser


class UserManager(Singleton):
    def __init__(self, db: PostgresAdapter = get_db_adapter()) -> None:
        self.db = db

    async def register_user(self, user: UserSchema) -> None:
        query = insert(DBUser).values(id=user.id, first_name=user.first_name)
        async with self.db.get_session() as session:
            try:
                await session.execute(query)
                await session.commit()
            except IntegrityError:
                await session.rollback()
