from pydantic import BaseModel

class Progress(BaseModel):
    ProgressID: int
    Progress: str