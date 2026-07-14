"""
Responsible for converting raw text into structured models.
"""

from app.models.document import Document


class DocumentParser:
    """Parses extracted text into a Document model."""

    def parse(self, text: str) -> Document:
        raise NotImplementedError