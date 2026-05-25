from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo
from core.config import settings


builder = InlineKeyboardBuilder()
builder.button(
    text="📊 Stats",
    callback_data="stats"
)
builder.button(
    text="🤖 Bot Settings",
    callback_data="bot_settings"
)
builder.button(
    text="🌐 Web App Settings",
    callback_data="web_app_settings"
)
builder.button(
    text="📣 Channel Settings",
    callback_data="channel_settings"
)

builder.adjust(1)