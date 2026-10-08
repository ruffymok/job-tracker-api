from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")

@app.get("/")
def read_root():
    return {"message": "Willkommen zur Job Tracker API!"}

@app.get("/applications")
def get_applications():
    return [
        {"id": 1, "company": "TechCorp", "status": "applied"},
        {"id": 2, "company": "Rheinmetall", "status": "interview"}
    ]