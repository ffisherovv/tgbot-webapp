from aiogram import F,Router
from aiogram.filters import CommandStart,Command,ContentType
from aiogram.types import Message,CallbackQuery
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Hello! Visit out website.",reply_markup=kb.markup)   

@router.message(F.content_type == ContentType.WEB_APP_DATA) 
async def webapp(message:Message):
    await message.answer(message.web_app_data.data)
    