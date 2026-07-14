from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        # Tries to safely read the file
        with open("index.html", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        # If it fails, it will display the exact error message on the screen
        return f"<h1>Server Error</h1><p>Details: {str(e)}</p><p>Current Folder Contents: {str(os.listdir('.'))}</p>"
