from typing import List
import uuid
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    cpf: str | None = None
    phone: str | None = None
    profile: str | None = None
    active: bool
    image_url: str | None = None
    password_hash: str


class UserCreate(UserBase):
    pass

class CarNested(BaseModel):
    id: uuid.UUID
    model: str
    license: str

    class Config:
        from_attributes = True

class UserOut(UserBase):
    id: uuid.UUID
    cars: List[CarNested] = []

    class Config:
        from_attributes = True
