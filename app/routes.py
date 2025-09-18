from fastapi import APIRouter
from .modules.auth import route as auth
from .modules.works import route as work
from .modules.cars import route as car
from .modules.jobs import route as job
from .modules.users import route as user
from .modules.statements import route as statement

router = APIRouter()
router.include_router(auth.router)
router.include_router(work.router)
router.include_router(user.router)
router.include_router(car.router)
router.include_router(job.router)
router.include_router(statement.router)

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
