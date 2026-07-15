import fitz

from app.models.document_info import DocumentInfo
from app.services.ocr import OCRService


class DocumentExtractor:

    def __init__(self):
        self.ocr = OCRService()

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
        """
        Public API.

        Determines the appropriate extraction strategy based on the
        document inspection results.
        """

        info = self.inspect(pdf_path)

        if info.requires_ocr:
            return self.extract_text_ocr(pdf_path)

        return self.extract_text_native(pdf_path)

    def extract_text_native(self, pdf_path: str) -> str:
        """
        Extract text directly from digitally generated PDFs.
        """

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        return text

    def extract_text_ocr(self, pdf_path: str) -> str:
        """
        Delegate OCR processing to the OCR service.
        """

        return self.ocr.extract(pdf_path)