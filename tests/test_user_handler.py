import pytest
# ============ USER HANDLERS ============


@pytest.mark.asyncio
async def test_start_handler_answers(mock_message):
    """
    /start bosganda message.answer chaqirilishi kerak
    """
    from handlers.user import start_handler

    await start_handler(mock_message)

    mock_message.answer.assert_called_once()


@pytest.mark.asyncio
async def test_start_handler_has_welcome_text(mock_message):
    """
    /start bosganda 'Welcome to GiftedForge' matni bo'lishi kerak
    """
    from handlers.user import start_handler

    await start_handler(mock_message)

    call_args = mock_message.answer.call_args[0][0]
    assert "Welcome to GiftedForge" in call_args


@pytest.mark.asyncio
async def test_start_handler_has_markup(mock_message):
    """
    /start bosganda keyboard berilishi kerak
    """
    from handlers.user import start_handler

    await start_handler(mock_message)

    call_kwargs = mock_message.answer.call_args[1]
    assert "reply_markup" in call_kwargs