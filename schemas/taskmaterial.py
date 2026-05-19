from pydantic import BaseModel
import datetime as dt

class TaskMaterialSchema(BaseModel):
    AufgabeID: int
    MaterialID: int
    Anzahl: int

class CreateTaskMaterialSchema(BaseModel):
    Anzahl: int