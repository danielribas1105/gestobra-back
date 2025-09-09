from datetime import datetime
from typing import Optional
import uuid
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import text

class Statement(SQLModel, table=True):
    __tablename__ = "statements"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    status: str = Field()
    
    job: Optional["Job"] = Relationship(back_populates="statement")