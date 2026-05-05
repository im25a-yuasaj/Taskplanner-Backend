from pydantic import BaseModel

class User(BaseModel):
    userID: int
    username: str
    usernPass: str