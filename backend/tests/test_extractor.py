from pathlib import Path

from app.services.extractor import DocumentExtractor


def test_document_inspection():
    extractor = DocumentExtractor()

    project_root = Path(__file__).resolve().parents[2]

    pdf_path = (
        project_root
        / "data"
        / "samples"
        / "rundfunk"
        / "festsetzungsbescheid"
        / "001.pdf"
    )

    assert pdf_path.exists()

    info = extractor.inspect(str(pdf_path))

    print(info)

    assert info.page_count > 0