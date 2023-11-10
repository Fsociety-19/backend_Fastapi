from pydantic import BaseModel
class Student(BaseModel):
    id:int
    dni:str
    name:str
    lastName:str
    numberPhone:str
