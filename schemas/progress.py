from pydantic import BaseModel

class ProgressSchema(BaseModel):
    FortschrittID: int
    Fortschritt: str