import pytest
# ============ ADMIN HANDLERS ============


@pytest.mark.asyncio
async def test_admin_handler_answers(mock_message):
    """
    /admin bosganda message.answer chaqirilishi kerak
    """
    from handlers.admin import admin_handler

    await admin_handler(mock_message)

    mock_message.answer.assert_called_once()


@pytest.mark.asyncio
async def test_admin_handler_welcome_text(mock_message):
    """
    /admin bosganda 'Welcome' matni bo'lishi kerak
    """
    from handlers.admin import admin_handler

    await admin_handler(mock_message)

    call_args = mock_message.answer.call_args[0][0]
    assert "Welcome" in call_args