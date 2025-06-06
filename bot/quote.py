from aiogram import Router, types
from aiogram.filters import Command
from quote_service import get_random_quote

router = Router()

@router.message(Command("quote"))
async def cmd_quote(message: types.Message):
    quote = get_random_quote()
    await message.answer(quote)
