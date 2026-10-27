from fastapi import FastAPI
from app.routers import applications

app = FastAPI(title="Job Tracker API")

app.include_router(applications.router)

@app.get("/")
def read_root():
    return {"message": "Willkommen zur aufgeräumten Job Tracker API!"}