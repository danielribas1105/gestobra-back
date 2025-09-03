from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    cpf: str
    phone: str
    profile: str
    status: str
    image_url: str
    password_hash: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: str

    class Config:
        orm_mode = True
