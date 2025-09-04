import uuid
from pydantic import BaseModel


class CarBase(BaseModel):
    model: str
    license: str
    driver: str
    manufacture: int | None = None
    km: int | None = None
    fuel: str | None = None
    strength: str | None = None
    capacity: str | None = None
    versatility: str | None = None
    active: bool
    image_url: str | None = None


class CarCreate(CarBase):
    pass


class CarOut(CarBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
