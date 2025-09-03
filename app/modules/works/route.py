from fastapi import APIRouter
from modules.works.model import Work
from modules.works.schema import Work as WorkSchema
from modules.works.service import (
   create_work,
   list_works
)

router = APIRouter(prefix="/work")