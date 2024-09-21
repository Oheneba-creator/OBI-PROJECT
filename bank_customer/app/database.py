from urllib import parse
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


USERNAME = "postgres.feouuwtusyryknzoyqvu"
PASSWORD = parse.quote_plus("1amadm1n2023")
DB_NAME = "postgres"
# postgres://postgres.feouuwtusyryknzoyqvu:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:5432/postgres

db_engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@aws-0-us-west-1.pooler.supabase.com:5432/{DB_NAME}")
# postgres://postgres.feouuwtusyryknzoyqvu:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:5432/postgres

Session = sessionmaker(bind=db_engine)

Base = declarative_base()

@contextmanager
def db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
        
