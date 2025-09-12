import uuid
from sqlalchemy.orm import Session
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from . import model, schema


def create_user(db: Session, user: schema.UserCreate):
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_users(db: Session):
    return db.query(model.User).all()

async def get_user_by_id(id: uuid.UUID | str | None):
    return await db.session.get(model.User, id)

async def get_user_by_email(email) -> model.User | None:
    result = (await db.session.execute(select(model.User).where(model.User.email == email))).first()

    return result[0] if result is not None else None


