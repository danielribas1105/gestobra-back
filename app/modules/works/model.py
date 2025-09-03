import uuid
from sqlmodel import SQLModel, Field
from sqlalchemy import text

class Work(SQLModel, table=True):
   __tablename__ = "works"

   id: uuid.UUID = Field(
      default_factory=uuid.uuid4,
      primary_key=True,
      sa_column_kwargs={"server_default": text("gen_random_uuid()")},
   )
   name: str = Field(index=True)
   description: str | None = Field(default=None)
   address: str | None = Field(default=None)
   region: str | None = Field(default=None)
   city: str | None = Field(default=None)
   state: str | None = Field(default=None)
   budget: str | None = Field(default=None)
   status: str | None = Field(default="ativa")
   image_url: str | None = Field(default=None)
