from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

sql_connection_string = os.getenv("SQLITE_CONNECTION")  # sqlite:///database.db

engine = create_engine(sql_connection_string, pool_size=30, max_overflow=0)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
