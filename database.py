from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Internal DB URL for Render internal communication
DATABASE_URL = "postgresql://leanlift_db_user:xk1jytwhle4zXHPmmGazqqjoXoUhIhny@dpg-d0j57k3e5dus73ai0adg-a/leanlift_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
