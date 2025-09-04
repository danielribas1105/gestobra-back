from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from .schema import CarCreate, CarOut
from .service import create_car, list_cars

router = APIRouter(prefix="/car", tags=["cars"])


@router.post("/", response_model=CarOut)
def create(car: CarCreate, db: Session=Depends(get_db)):
    return create_car(db, car)


@router.get("/", response_model=list[CarOut])
def list_all(db: Session=Depends(get_db)):
    return list_cars(db)
