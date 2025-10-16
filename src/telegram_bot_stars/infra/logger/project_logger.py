"""Заготовка под настроенный единый логгер для проекта"""
import logging
import sys

class ProjectLogger:
    def get_logger(self, name: str | None) -> logging.Logger:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        return logging.getLogger(name)