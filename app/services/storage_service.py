import os
import uuid
from pathlib import Path

UPLOAD_DIR = Path("uploads")
ALLOWED_EXTENSIONS = {"jpg", "png"}


def ensure_upload_dir() -> None:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_upload(file_bytes: bytes, extension: str) -> str:
    ensure_upload_dir()
    image_id = uuid.uuid4().hex
    file_path = UPLOAD_DIR / f"{image_id}.{extension}"
    with file_path.open("wb") as file_handle:
        file_handle.write(file_bytes)
    return image_id


def find_image_path(image_id: str) -> Path | None:
    for ext in ALLOWED_EXTENSIONS:
        candidate = UPLOAD_DIR / f"{image_id}.{ext}"
        if candidate.exists():
            return candidate
    return None
