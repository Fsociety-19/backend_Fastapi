from pydantic import BaseModel
class AuthShema(BaseModel):
    username:str
    password:str