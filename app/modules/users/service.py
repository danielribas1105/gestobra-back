from sqlalchemy.orm import Session
from . import model, schema


def create_user(db: Session, user: schema.UserCreate):
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def list_users(db: Session):
    return db.query(model.User).all()
