from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlmodel import select
from app.db.database import get_session
from app.modules.cars.model import Car

router = APIRouter(prefix="/car", tags=["cars"])

@router.post("/")
def create_car(car: Car, session: Session = Depends(get_session)):
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

@router.get("/")
def list_cars(session: Session = Depends(get_session)):
    cars = session.exec(select(Car)).all()
    return cars
