from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

URL_DATABASE = os.getenv("URL_DATABASE")

if URL_DATABASE is None:
    raise ValueError("URL_DATABASE environment variable is not set")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()