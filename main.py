# main.py
from fastapi import FastAPI
import models, db
import routes

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Trello Clone API"}
