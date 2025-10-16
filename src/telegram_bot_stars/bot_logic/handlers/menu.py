from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

menu_router = Router()


@menu_router.message(Command("menu"))
async def menu_command(message: Message) -> None:
    pass
