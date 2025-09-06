from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.database import engine
from .routes import router

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def home():
   return {"project": "GestObra"}
