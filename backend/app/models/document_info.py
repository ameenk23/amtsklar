from pydantic import BaseModel


class DocumentInfo(BaseModel):
    file_type: str

    page_count: int

    has_selectable_text: bool

    requires_ocr: bool

    image_quality: str

    is_blurry: bool

    is_rotated: bool

    rotation_angle: float | None = None

    language: str | None = None

    confidence: float