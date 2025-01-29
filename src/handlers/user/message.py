from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.dao import OrderDAO
from src.dao import UserDAO

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    if not UserDAO.is_exists(user_id=message.from_user.id):
        new_user = {
            'id': message.from_user.id,
            'is_bot': message.from_user.is_bot,
            'is_admin': False,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
        }
        UserDAO.add(**new_user)
        await message.answer('Добро пожаловать!')

    await message.answer(f'Привет {message.from_user.first_name}')


@router.message(Command("new_order"))
async def add_order(message: Message):
    new_order = {'user_id': message.from_user.id, }
    OrderDAO.add(**new_order)
    await message.answer('Ваш заказ успешно создан')


@router.message(Command("orders"))
async def get_orders(message: Message):
    orders = OrderDAO.get_user_orders(message.from_user.id)
    await message.answer('\n'.join([f'{order.id, order.status.value, order.created_at}' for order in orders]))

    @router.message()
    async def echo(message: Message):
        await message.answer(message.text)
