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


class UserOut(UserBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
