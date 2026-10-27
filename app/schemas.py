from typing import Optional
from pydantic import BaseModel, ConfigDict

class JobApplicationBase(BaseModel):
    company: str
    role: str
    status: str = "applied"

class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None

class JobApplicationResponse(JobApplicationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)