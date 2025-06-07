import os
import requests
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("metrics"))
async def cmd_metrics(message: types.Message):
    prom = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")
    url = f"{prom}/metrics"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
    except requests.RequestException:
        return await message.answer("Could not reach Prometheus `/metrics` endpoint.")

    text = resp.text.splitlines()
    preview = "\n".join(text[:20])
    if len(text) > 20:
        preview += "\n… (truncated)"

    await message.answer(f"Prometheus `/metrics`:\n```\n{preview}\n```", parse_mode="Markdown")
