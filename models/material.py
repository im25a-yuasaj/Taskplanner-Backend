from pydantic import BaseModel

class Material(BaseModel):
    MaterialID: int
    Material: str
    IsActive: bool