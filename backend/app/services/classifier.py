from app.models.enums import DocumentType


class DocumentClassifier:

    def classify(self, text: str) -> DocumentType:

        text = text.lower()

        if "festsetzungsbescheid" in text:
            return DocumentType.FESTSETZUNGSBESCHEID

        if "mahnung" in text:
            return DocumentType.MAHNUNG

        if "zahlungserinnerung" in text:
            return DocumentType.PAYMENT_REMINDER

        if "anmeldung" in text:
            return DocumentType.REGISTRATION

        return DocumentType.UNKNOWN