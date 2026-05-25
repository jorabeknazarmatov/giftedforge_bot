from aiogram import F, Router
from aiogram.types import Message
from middlewares.who import AdminFilter
from keyboards.admin_menu import builder
from core.logger import logger


router = Router()

@router.message(F.text == "/admin", AdminFilter())
async def admin_handler(message: Message) -> None:
    logger.info(f"Admin {message.from_user.id} joined admin panel")
    await message.answer(f"Welcome {message.from_user.full_name}, my boss!", reply_markup=builder.as_markup())
