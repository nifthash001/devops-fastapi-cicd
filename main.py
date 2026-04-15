from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel
import random
import string

app = FastAPI()

url_store = {}

class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while code in url_store:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_store[code] = request.url
    return {"short_code": code}

@app.get("/stats")
def get_stats():
    return {"total_urls": len(url_store), "urls": url_store}

@app.get("/{code}")
def redirect(code: str):
    if code not in url_store:
        raise HTTPException(status_code=404, detail="Code not found")
    return RedirectResponse(url_store[code])