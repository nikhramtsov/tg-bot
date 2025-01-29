import aiocron
from aiogram import Bot


from .dao import UserDAO
from .database import Session


@aiocron.crontab('0 8 * * *')
async def say_hello(bot: Bot):
    with Session() as session:
        users = UserDAO.get_all()
        for user in users:
            await bot.send_message(user.id, f'Hello, {user.first_name}!')
