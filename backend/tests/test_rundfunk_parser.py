from datetime import date

from app.parsers.rundfunk_parser import RundfunkParser
from app.services.extractor import DocumentExtractor

from tests.test_data import RUNDFUNK_FESTSETZUNGSBESCHEID_SAMPLE


def test_rundfunk_parser():

    extractor = DocumentExtractor()
    parser = RundfunkParser()

    text = extractor.extract_text(
        str(RUNDFUNK_FESTSETZUNGSBESCHEID_SAMPLE)
    )

    document = parser.parse(text)

    print(document)

    assert document.amount == 118.16

    assert (
        document.authority
        == "ARD ZDF Deutschlandradio Beitragsservice"
    )

    assert document.contribution_number == "5207993620"

    assert document.issue_date == date(2025, 5, 4)

    assert document.period_start == date(2025, 10, 1)

    assert document.period_end == date(2026, 3, 31)