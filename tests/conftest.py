# tests/test_handlers.py

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram.types import User, Chat


# ============ FIXTURES ============

@pytest.fixture
def mock_message():
    message = AsyncMock()
    message.answer = AsyncMock()
    message.delete = AsyncMock()
    message.from_user = MagicMock()
    message.from_user.id = 123456789
    message.from_user.full_name = "Test User"
    return message