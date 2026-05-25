from aiogram import Bot, Dispatcher
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    TG_ADMIN_IDS: list[int]
    WEB_APP_URL: str
    CHANNEL_URL: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()