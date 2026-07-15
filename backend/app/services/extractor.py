import fitz

from app.models.document_info import DocumentInfo


class DocumentExtractor:

    def inspect(self, pdf_path: str) -> DocumentInfo:
        document = fitz.open(pdf_path)

        has_selectable_text = False

        for page in document:
            if page.get_text().strip():
                has_selectable_text = True
                break

        return DocumentInfo(
            file_type="pdf",
            page_count=len(document),
            has_selectable_text=has_selectable_text,
            requires_ocr=not has_selectable_text,
            image_quality="unknown",
            is_blurry=False,
            is_rotated=False,
            rotation_angle=None,
            language=None,
            confidence=1.0
        )

    def extract_text(self, pdf_path: str) -> str:
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        return text