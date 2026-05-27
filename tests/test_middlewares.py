import pytest
from unittest.mock import AsyncMock, MagicMock
# ============ MIDDLEWARE ============


@pytest.mark.asyncio
async def test_role_middleware_admin():
    """
    Admin ID kelganda role='admin' bo'lishi kerak
    """
    from middlewares.who import RoleMiddleware
    from core.config import settings

    middleware = RoleMiddleware()
    handler = AsyncMock()

    event = MagicMock()
    data = {
        "event_from_user": MagicMock(id=settings.TG_ADMIN_IDS[0])
    }

    await middleware(handler, event, data)

    assert data["role"] == "admin"


@pytest.mark.asyncio
async def test_role_middleware_user():
    """
    Oddiy user kelganda role='user' bo'lishi kerak
    """
    from middlewares.who import RoleMiddleware

    middleware = RoleMiddleware()
    handler = AsyncMock()

    event = MagicMock()
    data = {
        "event_from_user": MagicMock(id=999999999)
    }

    await middleware(handler, event, data)

    assert data["role"] == "user"


@pytest.mark.asyncio
async def test_role_middleware_guest():
    """
    User ma'lumoti yo'q bo'lsa role='guest' bo'lishi kerak
    """
    from middlewares.who import RoleMiddleware

    middleware = RoleMiddleware()
    handler = AsyncMock()

    event = MagicMock()
    data = {}

    await middleware(handler, event, data)

    assert data["role"] == "guest"


# ============ ADMIN FILTER ============

@pytest.mark.asyncio
async def test_admin_filter_allows_admin():
    """
    Admin role bo'lsa filter True qaytarishi kerak
    """
    from middlewares.who import AdminFilter

    filter_ = AdminFilter()
    message = AsyncMock()

    result = await filter_(message, role="admin")

    assert result is True


@pytest.mark.asyncio
async def test_admin_filter_blocks_user():
    """
    User role bo'lsa filter False qaytarishi kerak
    """
    from middlewares.who import AdminFilter

    filter_ = AdminFilter()
    message = AsyncMock()

    result = await filter_(message, role="user")

    assert result is False