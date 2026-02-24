import os
from aiogram import Bot, Dispatcher, executor, types
from fastapi import FastAPI
import uvicorn
import asyncio

TOKEN = '8440176507:AAGzXvxlDM3TBUQVxAAOqx_hDvOew9zPWiI'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
app = FastAPI()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(types.KeyboardButton("Taqvimni ochish", web_app=types.WebAppInfo(url="")))
await message.answer("Xush kelibsiz!", reply_markup=markup)

@app.on_event("startup")
async def on_startup():
asyncio.create_task(dp.start_polling())

@app.get("/")
async def read_root():
return {"status": "Bot ishlayapti"}

if name == "main":
uvicorn.run(app, host="0.0.0.0", port=10000)
