from datetime import datetime

from pydantic import BaseModel

class Task(BaseModel):
    taskID: int
    title: str
    start: datetime
    end: datetime
    location: str
    coordinates: str
    note: str
    categoryID: str
    priorityID: int
    progressID: int
    userID: int