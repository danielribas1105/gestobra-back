from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlmodel import select
from app.db.database import get_session
from app.modules.users.model import User

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/")
def list_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users
