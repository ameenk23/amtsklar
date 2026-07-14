class Document(BaseModel):
    sender: str
    recipient: str
    document_type: str
    document_date: date | None = None
    reference_number: str | None = None
    raw_text: str