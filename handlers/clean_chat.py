from aiogram import F, Router
from aiogram.types import Message
from core.logger import logger


router = Router()

@router.message()
async def echo(message: Message) -> None:
    logger.debug("Junk message deleted")
    try:
        await message.delete()
    except Exception as e:
        logger.error(f"Error deleting message: {e}")