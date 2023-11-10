from pydantic import BaseModel
class CreateUser(BaseModel):
    username:str
    password:str
    idRol:str


class updateUserDetail(BaseModel):
    dni:str
    name:str
    lastName:str
    idUser:int
    