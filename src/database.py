from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from .conf import settings

DATABASE_URL = URL.create(
    'postgresql+psycopg2',
    username=settings.PG_USER,
    password=settings.PG_PASSWORD,
    host=settings.PG_HOST,
    database=settings.PG_DATABASE,
    port=settings.PG_PORT,
)

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(engine)
