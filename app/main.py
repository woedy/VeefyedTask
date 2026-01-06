import logging
from fastapi import FastAPI

from app.routes import upload, analyze
from app.services.storage_service import ensure_upload_dir

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Veefyed Skin Analysis API")


@app.on_event("startup")
def startup() -> None:
    ensure_upload_dir()


app.include_router(upload.router)
app.include_router(analyze.router)
