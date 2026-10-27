from fastapi import APIRouter
from app.models import JobApplication
from app.database import applications_db

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