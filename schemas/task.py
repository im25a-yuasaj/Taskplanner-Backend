from pydantic import BaseModel
import datetime as dt

class TaskSchema(BaseModel):
    AufgabeID: int
    Titel: str
    Beginn: dt.datetime
    Ende: dt.datetime
    Ort: str
    Koordinaten: str
    Notiz: str
    KategorieID: int
    PrioritaetID: int
    FortschrittID: int
    BenutzerID: int

class CreateTaskSchema(BaseModel):
    Titel: str
    Beginn: dt.datetime
    Ende: dt.datetime
    Ort: str
    Koordinaten: str
    Notiz: str
    KategorieID: int
    PrioritaetID: int
    FortschrittID: int
    BenutzerID: int