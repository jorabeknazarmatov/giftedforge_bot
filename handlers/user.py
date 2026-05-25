from aiogram import F, Router
from aiogram.types import Message
from keyboards.user_menu import builder
from core.logger import logger


router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message) -> None:
    logger.info(f"User {message.from_user.id} pressed start.")

    await message.answer(
        "Welcome to GiftedForge, a platform where talents, customers and digital collections meet instantly.\n\n"
        "Here your NFT/Gifts can become collectible.\n\n"
        "Добро пожаловать в GiftedForge — платформу, где таланты, клиенты и цифровые коллекции встречаются мгновенно.\n",

        reply_markup=builder.as_markup()
    )

