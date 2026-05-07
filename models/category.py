from pydantic import BaseModel

class Category(BaseModel):
    CategoryID: int
    Category: str
    IsActive: bool