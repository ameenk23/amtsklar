from pdf2image import convert_from_path
import pytesseract


class OCRService:
    """
    Performs OCR on scanned PDF documents.

    NOTE:
    Image enhancement (deskewing, denoising, contrast correction,
    blur detection, etc.) will be introduced incrementally as
    required by real-world documents.
    """

    def extract(self, pdf_path: str) -> str:

        pages = convert_from_path(pdf_path)

        extracted_text = []

        for page in pages:

            text = pytesseract.image_to_string(
                page,
                lang="deu"
            )

            extracted_text.append(text)

        return "\n".join(extracted_text)