from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    UserID: int
    UserName: str
    UserPWD: str

    model_config = ConfigDict(from_attributes=True)

class CreateUserSchema(BaseModel):
    UserName: str
    UserPWD: str

