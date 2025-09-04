from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from .schema import UserCreate, UserOut
from .service import create_user, list_users

router = APIRouter(prefix="/user", tags=["users"])


@router.post("/", response_model=UserOut)
def create(work: UserCreate, db: Session=Depends(get_db)):
    return create_user(db, work)


@router.get("/", response_model=list[UserOut])
def list_all(db: Session=Depends(get_db)):
    return list_users(db)
