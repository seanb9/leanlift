from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace the values below with yours (from the Render dashboard)
DATABASE_URL = "postgresql://leanlift_db_user:xKjjytwhle42XHPnmGazqojkXoUhJnhy@dpg-d0j57k3e6dus73ai0adg-a.frankfurt-postgres.render.com:5432/leanlift_db?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
