from fastapi import FastAPI
from starlette.responses import HTMLResponse

from app.routers import applications

app = FastAPI(title="Job Tracker API")

app.include_router(applications.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!doctype html>
    <html>
        <head>
            <title>Job Tracker API</title>
        </head>
        <body>
            <h1> Willkommen zur Job Tracker API </h1>
            <p> Zur interaktiven Dokumentation: </p>
            <a href="/docs"> Zu den API Docs (/docs)</a>
        </body>
    </html>
    """