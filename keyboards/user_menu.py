from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo
from core.config import settings


builder = InlineKeyboardBuilder()

builder.button(
    text="Open GiftedForge",
    web_app=WebAppInfo(url=settings.WEB_APP_URL)
)
builder.button(
    text="Join our channel",
    url=settings.CHANNEL_URL
)

builder.adjust(1)
