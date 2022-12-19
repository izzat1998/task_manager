from aiogram import types

start_menu = [
    [types.KeyboardButton(text="My Tasks"), ]
]
start_menu = types.ReplyKeyboardMarkup(keyboard=start_menu, resize_keyboard=True)
