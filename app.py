import asyncio
import logging
import warnings

import handlers, middlewares, states, filters
from middlewares import ThrottleMiddleware

from loader import dp, bot
from utils import create_table

warnings.filterwarnings("ignore")

async def main():
    await create_table()
    dp.update.middleware.register(ThrottleMiddleware())
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())