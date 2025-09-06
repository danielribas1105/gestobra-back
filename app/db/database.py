import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlmodel import Session

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

