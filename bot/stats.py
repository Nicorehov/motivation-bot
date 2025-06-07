from aiogram import Router, types
from aiogram.filters import Command
import requests
import os

router = Router()

@router.message(Command("stats"))
async def cmd_stats(message: types.Message):
    prom = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")
    query = "telegram_quote_requests_total"
    url = f"{prom}/api/v1/query?query={query}"
    resp = requests.get(url, timeout=5).json()

    if resp["status"] != "success":
        return await message.answer("Не удалось получить статистику.")

    value = resp["data"]["result"][0]["value"][1]
    await message.answer(f"Всего запросов /quote: {int(float(value))}")
