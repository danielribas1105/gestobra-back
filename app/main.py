from fastapi import FastAPI
""" from app import models, database """
from .routes import router

""" models.SQLModel.metadata.create_all(bind=database.engine) """

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
   return {"project": "GestObra"}
