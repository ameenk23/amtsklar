"""
Responsible for extracting raw text from uploaded documents.
"""


class DocumentExtractor:
    """Extracts text from PDFs or images."""

    def extract_text(self, file_path: str) -> str:
        raise NotImplementedError