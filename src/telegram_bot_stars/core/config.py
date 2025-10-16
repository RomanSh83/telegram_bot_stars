from logging import Logger

from dynaconf import Dynaconf

from telegram_bot_stars.core.base.singleton import Singleton
from telegram_bot_stars.infra.logger.project_logger import ProjectLogger


class Config(Singleton):
    settings = Dynaconf(environments=True, envvar_prefix="", settings_file=["config/settings.yaml"])
    logger = ProjectLogger()

def get_settings() -> Dynaconf:
    return Config.settings

def get_logger(name: str | None = None) -> Logger:
    if not name:
        name = __name__
    return Config.logger.get_logger(name=name)