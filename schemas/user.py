from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    BenutzerID: int
    BenutzerName: str
    BenutzerPWD: str

    class Config:
        from_attributes = True