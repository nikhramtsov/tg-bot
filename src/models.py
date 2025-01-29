import enum

from sqlalchemy import Column, BigInteger, Boolean, String, DateTime, ForeignKey, Enum, func
from sqlalchemy.orm import declarative_base, relationship, Mapped

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id: int = Column(BigInteger, primary_key=True)
    is_bot: bool = Column(Boolean)
    is_admin: bool = Column(Boolean)
    first_name: str = Column(String)
    last_name: str | None = Column(String, nullable=True)
    username: str | None = Column(String, nullable=True)
    orders = relationship('Order', back_populates='user')


class OrderStatus(enum.StrEnum):
    NEW = 'NEW'
    WAITING = 'WAITING'
    DELIVERED = 'DELIVERED'


class Order(Base):
    __tablename__ = "order"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    user: Mapped[User] = relationship(User, back_populates='orders')
    user_id: int = Column(BigInteger, ForeignKey('user.id'))
    created_at: DateTime = Column(DateTime, default=func.now())
    status: OrderStatus = Column(Enum(OrderStatus, name='order_status_enum'), default=OrderStatus.NEW)
    delivered_at: DateTime | None = Column(DateTime, default=None, nullable=True)
