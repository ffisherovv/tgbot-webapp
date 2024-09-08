import json
from aiogram import F, Router
from aiogram.filters import CommandStart, Command  # Исправлен импорт ContentTypes
from aiogram.types import Message,ContentType
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    
    await message.answer("Hello! Visit our website.", reply_markup=kb.markup)

@router.message(F.content_type == ContentType.WEB_APP_DATA)  # Используем ContentTypes
async def webapp(message: Message):
    res = json.loads()
    await message.answer(f'name:{res["name"]}\n email:{res["email"]}\n phone:{res["phone"]}')