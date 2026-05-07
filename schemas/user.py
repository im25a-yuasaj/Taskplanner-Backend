from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    BenutzerID: int
    BenutzerName: str
    BenutzerPWD: str

    model_config = ConfigDict(from_attributes=True)

class CreateUserSchema(BaseModel):
    BenutzerName: str
    BenutzerPWD: str

