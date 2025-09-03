from fastapi import FastAPI
from . import models, database, routes

models.SQLModel.metadata.create_all(bind=database.engine)


app = FastAPI()
app.include_router(routes.router)

@app.get("/")
def home():
    return {"project": "GestObra"}

@app.get("/soma")
def soma(a: int, b: int):
    return {"resultado": a + b}
