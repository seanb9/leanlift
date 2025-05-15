from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql://leanlift_db_user:xKijytwhle4zXHPnmGazqojkXoUhJhny@"
    "dpg-d0j57k3e6dus73ai0adg-a.frankfurt-postgres.render.com/leanlift_db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
