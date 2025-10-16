from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from telegram_bot_stars.bot_logic.keyboards.keyboards import open_menu_keyboard
from telegram_bot_stars.bot_logic.schemas.user_schemas import UserSchema
from telegram_bot_stars.infra.db.managers.user_managers import UserManager

simple_router = Router()

user_manager = UserManager()


@simple_router.message(Command("start"))
async def start_command(message: Message) -> None:
    user = UserSchema(id=message.from_user.id, first_name=message.from_user.first_name)
    await user_manager.register_user(user=user)
    await message.answer("Приветственное сообщение.", reply_markup=open_menu_keyboard)


@simple_router.message(Command("help"))
async def help_command(message: Message) -> None:
    pass


@simple_router.message(Command("about"))
async def about_command(message: Message) -> None:
    pass
