from sqlalchemy.exc import SQLAlchemyError

from src.database import Session


class BaseDAO:
    model = None

    @classmethod
    def add(cls, **values) -> model:
        new_instance = cls.model(**values)

        with Session() as session:
            session.add(new_instance)

            try:
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

            return new_instance

    @classmethod
    def get_by_id(cls, id: int) -> model:
        with Session() as session:
            try:
                instance = session.query(cls).filter_by(id=id).one()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

            return instance

    @classmethod
    def get_all(cls) -> list[model]:
        with Session() as session:
            try:
                instances = session.query(cls).all()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

            return instances