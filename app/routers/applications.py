from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

# Alle Bewerbungen abrufen
@router.get("/", response_model=List[schemas.JobApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    return db.query(models.JobApplicationModel).all()

# Einzelne Bewerbung über ID abrufen
@router.get("/{app_id}", response_model=schemas.JobApplicationResponse)
def get_application(app_id: int, db: Session = Depends(get_db)):
    app = db.query(models.JobApplicationModel).filter(models.JobApplicationModel.id == app_id).first()
    if not app:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bewerbung mit ID {app_id} wurde nicht gefunden."
        )
    return app

# Neue Bewerbung anlegen
@router.post("/", response_model=schemas.JobApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_application(application: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    db_app = models.JobApplicationModel(
        company=application.company,
        role=application.role,
        status=application.status
    )
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

# Bestehende Bewerbung aktualisieren
@router.put("/{app_id}", response_model=schemas.JobApplicationResponse)
def update_application(app_id: int, updated_data: schemas.JobApplicationUpdate, db: Session = Depends(get_db)):
    app_query = db.query(models.JobApplicationModel).filter(models.JobApplicationModel.id == app_id)
    app = app_query.first()

    if not app:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bewerbung mit ID {app_id} wurde nicht gefunden."
        )

    update_dict = updated_data.model_dump(exclude_unset=True)
    app_query.update(update_dict, synchronize_session=False)
    db.commit()
    db.refresh(app)
    return app

# Bewerbung löschen
@router.delete("/{app_id}", status_code=status.HTTP_200_OK)
def delete_application(app_id: int, db: Session = Depends(get_db)):
    app = db.query(models.JobApplicationModel).filter(models.JobApplicationModel.id == app_id).first()
    if not app:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bewerbung mit ID {app_id} wurde nicht gefunden."
        )
    db.delete(app)
    db.commit()
    return {"message": f"Bewerbung mit ID {app_id} erfolgreich gelöscht."}