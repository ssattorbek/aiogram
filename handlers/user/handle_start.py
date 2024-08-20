import asyncio

from aiogram.types import Message
from aiogram.filters import CommandStart

from loader import dp, bot
from utils import add_user

@dp.message(CommandStart())
async def handle_start(message: Message):
    await add_user(user_id=message.from_user.id, language=message.from_user.language_code)
    await bot.send_message(
        chat_id=message.chat.id,
        text="Привет, мир!"
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Привет! Этот бот помогает загружать IGTV, Reels, посты из <b>Instagram</b>. Пожалуйста, пришлите ссылку на СМИ в <b>Instagram</b>.",
    )
