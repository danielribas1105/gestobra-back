from __future__ import annotations
from typing import Optional
import uuid
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import text

class Car(SQLModel, table=True):
    __tablename__ = "cars"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    
    model: str = Field()
    license: str = Field(sa_column_kwargs={"unique": True, "index": True})
    driver_id: Optional[uuid.UUID] = Field(
        foreign_key="users.id", nullable=False, index=True
    ) 
    manufacture: int | None = Field(default=None)
    km: int | None = Field(default=None)
    fuel: str | None = Field(default=None)
    strength: str | None = Field(default=None)
    capacity: str | None = Field(default=None)
    versatility: str | None = Field(default=None)
    active: bool = Field(default=True, sa_column_kwargs={"server_default": "true"})
    image_url: str | None = Field(default=None)
    
    driver: "User" = Relationship(back_populates="cars")