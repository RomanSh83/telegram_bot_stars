from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

open_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Открыть меню")],
    ],
    resize_keyboard=True,
)
