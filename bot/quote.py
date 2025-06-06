from aiogram import Router, types
from quote_service import get_random_quote

router = Router()

@router.message(commands=["quote"])
async def cmd_quote(message: types.Message):
    quote = get_random_quote()
    await message.answer(quote)
