import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

import handlers
from config import Configs

logging.basicConfig(level=logging.INFO)


def register_routers(dp: Dispatcher) -> None:
    dp.include_routers(handlers.router)


async def main() -> None:
    session = AiohttpSession()
    bot = Bot(Configs().bot_token, session=session)
    dp = Dispatcher()
    register_routers(dp)
    try:
        await bot.delete_webhook()
        await asyncio.create_task(dp.start_polling(bot))

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    asyncio.run(main())
