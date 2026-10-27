from typing import Optional
from pydantic import BaseModel

# Modell zum Erstellen
class JobApplication(BaseModel):
    id: int
    company: str
    role: str
    status: str = "applied"

# Modell für Updates
class JobApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None