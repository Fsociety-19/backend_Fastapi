from fastapi import APIRouter
from pydantic import BaseModel
from services.status import Status
from Data.models.statusAppointModel import StatusAppointMent
from fastapi import FastAPI, Depends
from middleware.authMiddleware import AutorizationAdmin,AutorizationStaf,Authentication


status_router = APIRouter()
@status_router.get('/get/status', tags=["StatusAppointment"],dependencies=[Depends(Authentication())])
def get():
    return Status.getAll()

