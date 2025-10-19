import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from logging import getLogger

import handlers.admin.basic

from mongo.base import mongo

from config import (
    BOT_TOKEN,
    REDIS_PASSWORD,
)


logger = getLogger(__name__)

redis = Redis(host="redis", password=REDIS_PASSWORD, port=6379)
storage = RedisStorage(redis=redis)

dp = Dispatcher(storage=storage)

dp.include_routers(
    handlers.admin.basic.router,
)


async def on_startup():
    pass


dp.startup.register(on_startup)


async def main():
    logger.info("Bot is starting...")
    bot = Bot(token=BOT_TOKEN)
    mongo.test.test.insert_one({"Working": "True"})
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
