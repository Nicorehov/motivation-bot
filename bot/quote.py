from aiogram import Router, types
from aiogram.filters import Command
from quote_service import get_random_quote
from prometheus_client import Counter

router = Router()

messages_counter = Counter("telegram_quote_requests_total", 
                                "Total number of /quote command calls")

@router.message(Command("quote"))
async def cmd_quote(message: types.Message):
    messages_counter.inc()
    quote = get_random_quote()
    await message.answer(quote)