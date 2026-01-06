from fastapi import APIRouter, Depends, HTTPException

from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.analysis_service import analyze_image
from app.services.storage_service import find_image_path
from app.utils.validators import validate_api_key

router = APIRouter(tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_image_route(
    payload: AnalyzeRequest,
    _auth: None = Depends(validate_api_key),
) -> AnalyzeResponse:
    if not payload.image_id:
        raise HTTPException(status_code=400, detail="image_id is required")

    image_path = find_image_path(payload.image_id)
    if image_path is None:
        raise HTTPException(status_code=404, detail="image_id not found")

    result = analyze_image(payload.image_id)
    return AnalyzeResponse(image_id=payload.image_id, **result)
