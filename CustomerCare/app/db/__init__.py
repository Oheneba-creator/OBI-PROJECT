from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("postgresql+psycopg2://customer_care:Waptrck@localhost/customercaredb")

db_session = sessionmaker(bind=engine)

queue = []

def get_db():
    session = db_session()

    try:
        yield session
    except Exception as database_error:
        session.rollback()
        raise database_error
    finally:
        session.close()


class Base(DeclarativeBase):