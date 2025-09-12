from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from sqlmodel import select
from app.db.database import get_session
from app.modules.users.model import User
from app.modules.users import schema

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/", response_model=schema.UserOut)
def create_user(user: schema.UserCreate, session: Session = Depends(get_session)):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.get("/", response_model=list[schema.UserOut])
def list_users(session: Session = Depends(get_session)):
    statement = select(User)
    users = session.exec(statement).all()
    return users

@router.get("/{id}", response_model=schema.UserOut)
def get_user(id: str, session: Session = Depends(get_session)):
    statement = (
        select(User)
        .where(User.id == id)
    )
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user