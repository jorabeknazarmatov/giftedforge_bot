import pytest
# ============ CLEAN CHAT HANDLER ============


@pytest.mark.asyncio
async def test_echo_deletes_message(mock_message):
    """
    Noto'g'ri message kelganda o'chirilishi kerak
    """
    from handlers.clean_chat import echo

    await echo(mock_message)

    mock_message.delete.assert_called_once()


@pytest.mark.asyncio
async def test_echo_handles_delete_error(mock_message):
    """
    O'chirishda xato bo'lsa — crash bo'lmasligi kerak
    """
    from handlers.clean_chat import echo

    mock_message.delete.side_effect = Exception("Permission denied")

    # Xato bo'lsa ham crash bo'lmasin
    try:
        await echo(mock_message)
        assert True
    except Exception:
        assert False, "Handler should not raise exception"