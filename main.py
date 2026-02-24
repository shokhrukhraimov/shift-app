import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from aiogram import Bot, Dispatcher, types
from contextlib import asynccontextmanager

--- BOT SOZLAMALARI ---
TOKEN = '8440176507:AAGzXvxlDM3TBUQVxAAOqx_hDvOew9zPWiI'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
web_app = types.WebAppInfo(url="")
markup.add(types.KeyboardButton("📅 Smenani ko'rish", web_app=web_app))
await message.answer("Salom! Tizim 24/7 rejimida ishlamoqda.", reply_markup=markup)

--- FASTAPI SOZLAMALARI ---
@asynccontextmanager
async def lifespan(app: FastAPI):
asyncio.create_task(dp.start_polling())
yield
await bot.session.close()

app = FastAPI(lifespan=lifespan)

try:
app.mount("/static", StaticFiles(directory="static"), name="static")
except:
pass

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health():
return {"status": "ok"}