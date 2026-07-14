class RundfunkDocument(Document):
    beitragsnummer: str | None = None

    payment_period_start: date | None = None
    payment_period_end: date | None = None

    amount_due: float | None = None

    includes_late_fee: bool = False

    enforcement_warning: bool = False