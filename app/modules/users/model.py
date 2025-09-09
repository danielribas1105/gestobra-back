from __future__ import annotations
from typing import List
import uuid
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import text

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    name: str = Field()
    email: str = Field(sa_column_kwargs={"unique": True, "index": True})
    cpf: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    profile: str | None = Field(default="user")
    active: bool = Field(default=True, sa_column_kwargs={"server_default": "true"})
    image_url: str | None = Field(default=None)
    password_hash: str = Field()

    cars: List["Car"] = Relationship(back_populates="driver")
    jobs: List["Job"] = Relationship(back_populates="user")