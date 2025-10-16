import asyncio
import logging
import sys
from contextlib import asynccontextmanager

from telegram_bot_stars.bot_logic.handlers.events import start_bot, stop_bot
from telegram_bot_stars.bot_logic.handlers.simple import simple_router
from telegram_bot_stars.infra.telegram.bot_core import (
    get_bot,
    get_dp,
    get_fmc_storage,
)

bot = get_bot()
dp = get_dp()
storage = get_fmc_storage()


@asynccontextmanager
async def lifespan():
    yield
    await storage.close()


async def main() -> None:
    async with lifespan():
        dp.include_router(simple_router)
        dp.startup.register(start_bot)
        dp.shutdown.register(stop_bot)
        async with bot:
            await dp.start_polling(bot)


def run_app() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


if __name__ == "__main__":
    run_app()
