from pydantic import BaseModel

class WorkBase(BaseModel):
   name: str
   description: str
   address: str
   region: str
   city: str
   state: str
   budget: str
   active: bool
   image_url: str

class WorkCreate(WorkBase):
   pass

class WorkOut(WorkBase):
   id: str

   class Config:
      orm_mode = True
