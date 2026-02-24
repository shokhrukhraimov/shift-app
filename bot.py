from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import WebAppInfo

# BotFather'dan olgan tokenni shu yerga qo'ying
TOKEN = '8440176507:AAGzXvxlDM3TBUQVxAAOqx_hDvOew9zPWiI'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Sizning oxirgi ngrok linkingiz:
    web_app = WebAppInfo(url="https://ami-uncurtainable-arvilla.ngrok-free.dev")
    
    # DIQQAT: Bu qator tepadagilar bilan bir xil darajada turishi shart!
    markup.add(types.KeyboardButton(text="📅 Smenani ko'rish", web_app=web_app))
    
    await message.answer(f"Salom {message.from_user.full_name}!\nSmena tizimi tayyor.", reply_markup=markup)

if __name__ == '__main__':
    print("Bot ishga tushmoqda...")
    executor.start_polling(dp, skip_updates=True)