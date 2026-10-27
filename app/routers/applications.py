from fastapi import APIRouter, HTTPException, status
from app.models import JobApplication, JobApplicationUpdate
from app.database import applications_db

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

# Alle Bewerbungen abrufen
@router.get("/")
def get_applications():
    return applications_db

# Eine einzelne Bewerbung über ihre ID abrufen
@router.get("/{app_id}")
def get_application(app_id: int):
    for app in applications_db:
        if app.id == app_id:
            return app
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Bewerbung mit ID {app_id} wurde nicht gefunden."
    )

# Neue Bewerbung anlegen
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_application(application: JobApplication):
    for app in applications_db:
        if app.id == application.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Eine Bewerbung mit ID {application.id} existiert bereits."
            )
    applications_db.append(application)
    return {"message": "Bewerbung erfolgreich hinzugefügt!", "data": application}

# Bestehende Bewerbung aktualisieren (z. B. Status ändern)
@router.put("/{app_id}")
def update_application(app_id: int, updated_data: JobApplicationUpdate):
    for app in applications_db:
        if app.id == app_id:
            if updated_data.company is not None:
                app.company = updated_data.company
            if updated_data.role is not None:
                app.role = updated_data.role
            if updated_data.status is not None:
                app.status = updated_data.status
            return {"message": "Bewerbung aktualisiert!", "data": app}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Bewerbung mit ID {app_id} wurde nicht gefunden."
    )

# Bewerbung löschen
@router.delete("/{app_id}")
def delete_application(app_id: int):
    for index, app in enumerate(applications_db):
        if app.id == app_id:
            deleted_app = applications_db.pop(index)
            return {"message": "Bewerbung gelöscht!", "data": deleted_app}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Bewerbung mit ID {app_id} wurde nicht gefunden."
    )