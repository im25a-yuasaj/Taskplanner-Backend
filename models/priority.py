from pydantic import BaseModel

class Priority(BaseModel):
    PriorityID: int
    Priority: str