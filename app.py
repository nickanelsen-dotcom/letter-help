from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    """
    This function listens for anyone visiting your Render web address,
    safely opens your index.html file, and serves it to their screen.
    """
    try:
        with open("index.html", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>Initialization Error</h1><p>The index.html file could not be located in the root repository folder.</p>"
