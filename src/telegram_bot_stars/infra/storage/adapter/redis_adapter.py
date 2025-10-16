from contextlib import asynccontextmanager

import redis.asyncio as redis
from redis.asyncio.connection import ConnectionPool

from telegram_bot_stars.core.base.singleton import Singleton
from telegram_bot_stars.core.config import get_settings


class RedisAdapter(Singleton):
    def __init__(self):
        self.connection_pool = ConnectionPool.from_url(
            url=get_settings().REDIS_URL,
            max_connections=get_settings().REDIS_MAX_CONNECTIONS,
            decode_responses=True,
            encoding="utf-8",
        )

    def get_client(self) -> redis.Redis:
        return redis.Redis(connection_pool=self.connection_pool)

    @asynccontextmanager
    async def redis_client(self):
        client = redis.Redis(connection_pool=self.connection_pool)
        try:
            yield client
        finally:
            await client.aclose()


def get_broker_adapter() -> RedisAdapter:
    return RedisAdapter()
