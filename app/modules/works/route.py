from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from .schema import WorkCreate, WorkOut
from .service import create_work, list_works

router = APIRouter(prefix="/work", tags=["works"])


@router.post("/", response_model=WorkOut)
def create(work: WorkCreate, db: Session=Depends(get_db)):
    return create_work(db, work)


@router.get("/", response_model=list[WorkOut])
def list_all(db: Session=Depends(get_db)):
    return list_works(db)
