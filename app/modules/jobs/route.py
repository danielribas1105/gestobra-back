from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from .schema import JobCreate, JobOut
from .service import create_job, list_jobs

router = APIRouter(prefix="/job", tags=["jobs"])


@router.post("/", response_model=JobOut)
def create(work: JobCreate, db: Session=Depends(get_db)):
    return create_job(db, work)


@router.get("/", response_model=list[JobOut])
def list_all(db: Session=Depends(get_db)):
    return list_jobs(db)
