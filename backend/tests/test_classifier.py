from app.services.classifier import DocumentClassifier
from app.models.enums import DocumentType

classifier = DocumentClassifier()

sample_text = """
Westdeutscher Rundfunk Köln

Festsetzungsbescheid

Sehr geehrte Frau...
"""

result = classifier.classify(sample_text)

print(result)

assert result == DocumentType.FESTSETZUNGSBESCHEID

print("✅ Classifier test passed.")