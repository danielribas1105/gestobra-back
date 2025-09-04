import uuid
from sqlmodel import SQLModel, Field
from sqlalchemy import text

class Job(SQLModel, table=True):
    __tablename__ = "jobs"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    created_at: str = Field()
    updated_at: str = Field()
    origin: str = Field()
    destiny: str = Field()
    car_id: str = Field()
    user_id: str = Field()
    m3: int = Field()
    status: str = Field()