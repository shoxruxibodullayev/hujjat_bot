import asyncio
import os
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
)
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta, timezone

# ✅ .env dan tokenlar va sozlamalar
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
ADMIN_TIMEOUT = timedelta(minutes=30)
ADMIN_PHONE = os.getenv("ADMIN_PHONE")
ADMIN_TELEGRAM = os.getenv("ADMIN_TELEGRAM")

# 🔐 Firebase sertifikatini JSON string sifatida olish
import json
cred_json = json.loads(os.getenv("FIREBASE_CREDENTIALS_JSON"))
cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred)
db = firestore.client()

# 🔁 Bot sozlash
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# 🕒 Admin sessiyalar
admin_sessions = {}

# (Bu yerga sizning qolgan kodlaringiz keladi — siz avval yuborgan `bot.py`)

# ▶️ Botni ishga tushurish
async def main():
    print("🚀 Bot ishga tushmoqda... Ctrl+C bosib to‘xtatishingiz mumkin.")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Botda xatolik: {e}")

if __name__ == "__main__":
    asyncio.run(main())
