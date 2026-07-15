from pathlib import Path

from app.models.enums import DocumentType
from app.services.classifier import DocumentClassifier
from app.services.extractor import DocumentExtractor
from tests.conftest import SAMPLE_RUNDFUNK

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SAMPLE = (
    PROJECT_ROOT
    / "data"
    / "samples"
    / "rundfunk"
    / "festsetzungsbescheid"
    / "sample_001.pdf"
)


def test_rundfunk_pipeline():

    extractor = DocumentExtractor()
    classifier = DocumentClassifier()

    text = extractor.extract_text(str(SAMPLE))

    print("\n===== Extracted Text =====\n")
    print(text[:1000])

    document_type = classifier.classify(text)

    print(f"\nDetected: {document_type}")

    assert document_type == DocumentType.FESTSETZUNGSBESCHEID