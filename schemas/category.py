from pydantic import BaseModel, ConfigDict

class CategorySchema(BaseModel):
    KategorieID: int
    Kategorie: str
    IstAktiv: bool

    model_config = ConfigDict(from_attributes=True)

class CreateCategorySchema(BaseModel):
    Kategorie: str
    IstAktiv: bool