from pydantic import BaseModel


class Decision(BaseModel):
    risk: str
    action: str
    explanation: str
    next_stage: str | None = None