```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Looks inside your project folder and safely opens index.html
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()