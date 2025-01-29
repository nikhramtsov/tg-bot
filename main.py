import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession

from src.conf import settings
from src.handlers import router
from src.tasks import say_hello

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    session = AiohttpSession()
    bot = Bot(
        token=settings.BOT_TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode='HTML'),
    )

    dp = Dispatcher()
    dp['bot'] = bot
    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(e)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    say_hello.start()
    asyncio.run(main())
