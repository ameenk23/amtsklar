"""
Responsible for determining what the user should do next.
"""

from app.models.document import Document
from app.models.decision import Decision


class DecisionEngine:
    """Produces a decision based on a parsed document."""

    def evaluate(self, document: Document) -> Decision:
        raise NotImplementedError