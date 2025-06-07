import os

import requests
from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("stats"))
async def cmd_stats(message: types.Message):
    prom = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")
    query = "telegram_quote_requests_total"
    url = f"{prom}/api/v1/query?query={query}"
    resp = requests.get(url, timeout=5).json()

    if resp.get("status") != "success":
        await message.answer("Could not get stats.")
        return

    value = resp["data"]["result"][0]["value"][1]
    count = int(float(value))
    await message.answer(f"Overall number of /quote calls: {count}")
