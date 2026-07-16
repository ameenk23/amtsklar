from datetime import date

from pydantic import BaseModel

from app.models.enums import DocumentType


class RundfunkDocument(BaseModel):

    document_type: DocumentType

    authority: str | None = None

    contribution_number: str |None = None

    issue_date: date | None = None

    period_start: date | None = None

    period_end: date | None = None

    amount: float | None = None