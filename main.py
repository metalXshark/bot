import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

API_TOKEN = '7324883600:AAGAte1fdWr-yTTwH1dsMDIn5Ze4DII-JBY'
ADMIN_ID = 1031182339  # Укажите ID администратора

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        # Создаем кнопку для администратора
        await message.answer(f'Здравствуйте, {user_name}!')
    else:
        # Создаем онлайн-кнопку для клиента
        button = InlineKeyboardButton(
            text='Перейти в магазин',
            web_app=WebAppInfo(url='https://metalxshark.github.io/pageBot/')
        )
        markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
        await message.answer(f'Здравствуйте, {user_name}!', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())