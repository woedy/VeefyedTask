import os
from typing import Tuple

from fastapi import Header, HTTPException, UploadFile

MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_CONTENT_TYPES = {
    "image/jpeg": "jpg",
    "image/png": "png",
}


def validate_api_key(x_api_key: str | None = Header(default=None)) -> None:
    required_key = os.getenv("API_KEY")
    if required_key and x_api_key != required_key:
        raise HTTPException(status_code=401, detail="Invalid API key")


async def validate_upload(upload_file: UploadFile) -> Tuple[bytes, str]:
    if upload_file.content_type not in ALLOWED_CONTENT_TYPES:
        raise ValueError("Only JPEG and PNG images are allowed")

    file_bytes = await upload_file.read()
    if not file_bytes:
        raise ValueError("Uploaded file is empty")

    if len(file_bytes) > MAX_FILE_SIZE:
        raise ValueError("File size exceeds 5MB limit")

    extension = ALLOWED_CONTENT_TYPES[upload_file.content_type]
    return file_bytes, extension
