import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from aiogram import Bot, Dispatcher, types
from contextlib import asynccontextmanager

# --- BOT SOZLAMALARI ---
TOKEN = 'SIZNING_BOT_TOKENINGIZ'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Bu yerga Render beradigan linkni keyinroq qo'yamiz
    web_app = types.WebAppInfo(url="https://shift-app.onrender.com") 
    markup.add(types.KeyboardButton("📅 Smenani ko'rish", web_app=web_app))
    await message.answer("Salom! Tizim 24/7 rejimida ishlamoqda.", reply_markup=markup)

# --- FASTAPI SOZLAMALARI ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Botni orqa fonda ishga tushirish
    asyncio.create_task(dp.start_polling())
    yield
    # To'xtaganda botni ham o'chirish
    await bot.session.close()

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health():
    return {"status": "ok"}