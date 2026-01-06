from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.models.schemas import UploadResponse
from app.services.storage_service import save_upload
from app.utils.validators import validate_api_key, validate_upload

router = APIRouter(tags=["upload"])


@router.post("/upload", response_model=UploadResponse)
async def upload_image(
    file: UploadFile = File(...),
    _auth: None = Depends(validate_api_key),
) -> UploadResponse:
    try:
        file_bytes, extension = await validate_upload(file)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    image_id = save_upload(file_bytes, extension)
    return UploadResponse(image_id=image_id)
