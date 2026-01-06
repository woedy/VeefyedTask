from typing import List

from pydantic import BaseModel


class UploadResponse(BaseModel):
    image_id: str


class AnalyzeRequest(BaseModel):
    image_id: str | None = None


class AnalyzeResponse(BaseModel):
    image_id: str
    skin_type: str
    issues: List[str]
    confidence: float
