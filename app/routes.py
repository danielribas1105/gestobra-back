from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal
import modules.works.route as work

router = APIRouter()

router.include_router(work.router, tags=["work"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.list_users(db)
