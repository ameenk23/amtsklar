from pathlib import Path
from tests.conftest import SAMPLE_RUNDFUNK
from app.services.extractor import DocumentExtractor


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SAMPLE_PDF = (
    PROJECT_ROOT
    / "data"
    / "samples"
    / "rundfunk"
    / "festsetzungsbescheid"
    / "sample_001.pdf"
)


def test_document_inspection():
    extractor = DocumentExtractor()

    assert SAMPLE_PDF.exists(), f"Sample PDF not found: {SAMPLE_PDF}"

    info = extractor.inspect(str(SAMPLE_PDF))

    print(info)

    assert info.page_count > 0


def test_extract_text():

    extractor = DocumentExtractor()

    info = extractor.inspect(str(SAMPLE_PDF))

    text = extractor.extract_text(str(SAMPLE_PDF))

    if info.requires_ocr:
        assert len(text.strip()) > 0