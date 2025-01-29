from sqlalchemy import select, exists

from base.dao import BaseDAO
from .models import Order, User
from .database import Session


class OrderDAO(BaseDAO):
    model = Order

    @classmethod
    def get_user_orders(cls, user_id):
        query = select(Order).where(Order.user_id == user_id)
        with Session() as session:
            return session.execute(query).scalars().all()


class UserDAO(BaseDAO):
    model = User

    @classmethod
    def is_exists(cls, user_id: int) -> bool:
        query = select(exists().where(User.id == user_id))
        with Session() as session:
            return session.execute(query).scalar()
