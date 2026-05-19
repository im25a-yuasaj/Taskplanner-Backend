'''
Here are the schemas for the file table
'''
from pydantic import BaseModel

class FileSchema(BaseModel):
    '''
    This class is used for the file table
    '''
    DateiID: int
    AufgabeID: int
    Dateipfad: str
    DateiBLOB: bytes

class CreateFileSchema(BaseModel):
    '''
    Here is the schema for adding files to the database
    '''
    AufgabeID: int
    Dateipfad: str