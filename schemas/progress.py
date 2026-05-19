'''
Here are the schemas for the progress table
'''
from pydantic import BaseModel

class ProgressSchema(BaseModel):
    '''
    This is the schema for the progress table
    '''
    FortschrittID: int
    Fortschritt: str

class CreateProgressSchema(BaseModel):
    '''
    This is the schema for creating a new progress
    '''
    Fortschritt: str