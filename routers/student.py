from fastapi import APIRouter
from pydantic import BaseModel
from schema.students import Student



student_router = APIRouter()
@student_router.post('/create/student', tags=["Students"])
def create(student:Student):
    return True

