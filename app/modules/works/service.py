from sqlalchemy.orm import Session
from . import models, schemas
from modules.works.model import Work

async def create_work(db: Session, work: schemas.UserCreate) -> Work:
   newWork = Work(**work.dict())
   db.add(newWork)
   await db.commit()
   await db.refresh(newWork)
   return newWork

def list_works(db: Session):
   return db.query(models.User).all()
