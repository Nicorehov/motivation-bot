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

    try:
        resp = requests.get(url, timeout=5).json()
    except requests.RequestException:
        return await message.answer("Could not reach Prometheus.")

    results = resp.get("data", {}).get("result", [])
    if resp.get("status") != "success" or not results:
        return await message.answer("No quote stats available yet.")

    value = results[0]["value"][1]
    try:
        count = int(float(value))
    except (ValueError, TypeError):
        return await message.answer("Got unexpected data format from Prometheus.")

    await message.answer(f"Total `/quote` calls: {count}")