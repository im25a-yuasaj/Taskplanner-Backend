from pydantic import BaseModel, ConfigDict

class MaterialSchema(BaseModel):
    MaterialID: int
    Material: str
    IstAktiv: bool

    model_config = ConfigDict(from_attributes=True)

class CreateMaterialSchema(BaseModel):
    Material: str
    IstAktiv: bool