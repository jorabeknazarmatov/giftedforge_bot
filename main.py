from middlewares.who import RoleMiddleware
from handlers import user, admin, clean_chat
from core.config import bot, dp
from core.logger import logger
import asyncio


async def main() -> None:
    logger.info("Starting bot...")

    dp.update.outer_middleware(RoleMiddleware())
    dp.include_router(user.router)
    dp.include_router(admin.router)
    dp.include_router(clean_chat.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())