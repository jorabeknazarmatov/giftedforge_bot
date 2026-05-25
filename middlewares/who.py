from aiogram import BaseMiddleware
from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject, Message
from typing import Any, Awaitable, Callable, Dict
from core.config import settings


class RoleMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user = data.get("event_from_user")

        if user:
            if user.id in settings.TG_ADMIN_IDS:
                data["role"] = "admin"
            else:
                data["role"] = "user"
        else:
            data["role"] = "guest"

        return await handler(event, data)

class AdminFilter(BaseFilter):
    async def __call__(self, message: Message, role: str) -> bool:
        return role == "admin"