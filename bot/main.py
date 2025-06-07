import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from quote import router
from prometheus_client import Counter, start_http_server
from stats import router as stats_router


load_dotenv()    

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    bot = Bot(token=BOT_TOKEN)

    start_http_server(8000)

    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(stats_router)

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
