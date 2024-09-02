from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Перейти на веб-сайт.',web_app=WebAppInfo(url='https://ffisherovv.github.io/tgbot-webapp/'))]
])