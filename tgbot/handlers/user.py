from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import start_menu


async def user_start(message: Message):
    await message.reply("Hello22, user!", reply_markup=start_menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
