import asyncio
import logging

from aiogram import Bot,Dispatcher,F
from dotenv import load_dotenv
import os


from app.handlers import router


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()





async def main():
    load_dotenv()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')