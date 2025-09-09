from datetime import datetime
from typing import Optional
import uuid
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import text

class Job(SQLModel, table=True):
    __tablename__ = "jobs"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    origin: Optional[uuid.UUID] = Field(
        foreign_key="works.id", nullable=False, index=True
    )
    destiny: Optional[uuid.UUID] = Field(
        foreign_key="works.id", nullable=False, index=True
    )
    car_id: Optional[uuid.UUID] = Field(
        foreign_key="cars.id", nullable=False, index=True
    )
    user_id: Optional[uuid.UUID] = Field(
        foreign_key="users.id", nullable=False, index=True
    ) 
    statement_id: Optional[uuid.UUID] = Field(
        foreign_key="statements.id", nullable=False, index=True, unique=True
    ) 
    m3: int = Field()
    status: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    
    car: Optional["Car"] = Relationship(back_populates="jobs")
    user: Optional["User"] = Relationship(back_populates="jobs")
    statement: Optional["Statement"] = Relationship(back_populates="job")
    origin_work: Optional["Work"] = Relationship(back_populates="jobs_origin", sa_relationship_kwargs={"foreign_keys": "[Job.origin]"})
    destiny_work: Optional["Work"] = Relationship(back_populates="jobs_origin", sa_relationship_kwargs={"foreign_keys": "[Job.destiny]"})