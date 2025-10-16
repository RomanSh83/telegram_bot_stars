import logging

from telegram_bot_stars.bot_logic.commands.commands import set_commands
from telegram_bot_stars.core.config import get_settings
from telegram_bot_stars.infra.telegram.bot_core import get_bot

bot = get_bot()
logger = logging.getLogger(__name__)


async def start_bot() -> None:
    logger.info("Starting bot")
    await set_commands(bot=get_bot())
    for admin_id in get_settings().ADMINS:
        await get_bot().send_message(admin_id, "Bot is started.")


async def stop_bot():
    logger.info("Stopping bot")
    for admin_id in get_settings().ADMINS:
        await get_bot().send_message(admin_id, "Bot is stopped.")
