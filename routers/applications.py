from fastapi import APIRouter
from models import JobApplication
from database import applications_db

# Wir erstellen einen Router, bei dem alle Routen mit "/applications" beginnen
router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.get("/")
def get_applications():
    return applications_db

@router.post("/")
def create_application(application: JobApplication):
    applications_db.append(application)
    return {"message": "Bewerbung hinzugefügt!", "data": application}