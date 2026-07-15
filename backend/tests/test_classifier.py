from app.models.enums import DocumentType
from app.services.classifier import DocumentClassifier


def test_classifier():

    classifier = DocumentClassifier()

    sample_text = """
    Westdeutscher Rundfunk Köln

    Festsetzungsbescheid
    """

    result = classifier.classify(sample_text)

    assert result == DocumentType.FESTSETZUNGSBESCHEID