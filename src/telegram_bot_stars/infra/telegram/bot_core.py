from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage

from telegram_bot_stars.core.config import get_settings
from telegram_bot_stars.infra.storage.adapter.redis_adapter import RedisAdapter


class BotCore:
    bot = Bot(token=get_settings().TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    storage = RedisStorage(redis=RedisAdapter().get_client())
    dp = Dispatcher(storage=storage)


def get_bot() -> Bot:
    return BotCore.bot


def get_dp() -> Dispatcher:
    return BotCore.dp


def get_fmc_storage() -> RedisStorage:
    return BotCore.storage
