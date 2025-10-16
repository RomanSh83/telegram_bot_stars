import logging

from telegram_bot_stars.core.run import run_app

logger = logging.getLogger(__name__)

def run():
    # logging.info("Bot started.")
    run_app()
    # logging.info("Bot stopped.")