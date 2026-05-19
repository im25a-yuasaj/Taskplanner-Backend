from pydantic import BaseModel

class FileSchema(BaseModel):
    DateiID: int
    AufgabeID: int
    Dateipfad: str
    DateiBLOB: bytes

class CreateFileSchema(BaseModel):
    AufgabeID: int
    Dateipfad: str