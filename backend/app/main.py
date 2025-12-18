from fastapi import FastAPI
from app.routers import ocr

app = FastAPI(title="AI Scan & Translate API")

app.include_router(ocr.router)

@app.get("/")
def root():
    return {"status": "API running"}
