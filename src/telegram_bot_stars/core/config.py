from dynaconf import Dynaconf

from telegram_bot_stars.core.base.singleton import Singleton


class Config(Singleton):
    settings = Dynaconf(environments=True, envvar_prefix="", settings_file=["config/settings.yaml"])


def get_settings() -> Dynaconf:
    return Config.settings
