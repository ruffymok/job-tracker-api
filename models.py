from pydantic import BaseModel

class JobApplication(BaseModel):
    id: int
    company: str
    role: str
    status: str = "applied"