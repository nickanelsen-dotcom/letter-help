from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Replace the link below with your actual CodePen "Full Page View" or "Debug View" URL
    codepen_url = "https://codepen.io"
    
    try:
        # This automatically grabs your perfect, working frontend layout from CodePen
        response = requests.get(codepen_url)
        return response.text
    except Exception as e:
        return f"<h1>App Loading...</h1><p>Ensure your CodePen link is correct.</p>"
