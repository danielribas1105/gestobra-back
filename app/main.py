import datetime
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.database import engine
from .routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ou ["*"] durante dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def home():
   return {"project": "GestObra"}

@app.get("/status")
def get_status():
    return {
        "status": "online",
        "timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
