from pydantic import BaseModel, ConfigDict

class PrioritySchema(BaseModel):
    PrioritaetID: int
    Prioritaet: str

    model_config = ConfigDict(from_attributes=True)

class CreatePrioritySchema(BaseModel):
    Prioritaet: str