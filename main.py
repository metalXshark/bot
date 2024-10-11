import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from keep_alive import keep_alive

# Получение токена и ID администратора из переменных окружения
API_TOKEN = os.getenv('API_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))  # Убедитесь, что ADMIN_ID является целым числом

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        # Сообщение для администратора
        await message.answer(f'Здравствуйте, {user_name}! Это сообщение для администратора.')
    else:
        # Онлайн-кнопка для клиента
        button = InlineKeyboardButton(
            text='Перейти в магазин',
            web_app=WebAppInfo(url='https://metalxshark.github.io/pageBot/')
        )
        markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
        await message.answer(f'Здравствуйте, {user_name}!', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    keep_alive()  # Запуск веб-сервера для поддержки работы на Render.com
    asyncio.run(main())
