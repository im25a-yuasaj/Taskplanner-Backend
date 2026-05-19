'''
Here are the schemas for the user
'''
from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    '''
    This is the main schema for the user
    '''
    BenutzerID: int
    BenutzerName: str
    BenutzerPWD: str

    model_config = ConfigDict(from_attributes=True)

class CreateUserSchema(BaseModel):
    '''
    This is the schema for inserting a new user into the database
    '''
    BenutzerName: str
    BenutzerPWD: str