'''
This file contains the TaskSchema and CreateTaskSchema classes.
'''
from pydantic import BaseModel
import datetime as dt

class TaskSchema(BaseModel):
    '''
    This is the schema for the task.
    '''
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
    '''
    This schema is used for adding a new task to the database.
    '''
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