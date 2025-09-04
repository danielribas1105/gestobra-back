from fastapi import APIRouter
from .modules.works import route as work
from .modules.users import route as user
from .modules.cars import route as car

router = APIRouter()
router.include_router(work.router)
router.include_router(user.router)
router.include_router(car.router)

""" router = APIRouter()

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
 """
