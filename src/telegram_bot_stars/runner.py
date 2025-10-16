import logging

from telegram_bot_stars.core.config import get_logger
from telegram_bot_stars.core.run import run_app

logger = get_logger()

def run():
    logging.info("Bot started.")
    run_app()
    logging.info("Bot stopped.")