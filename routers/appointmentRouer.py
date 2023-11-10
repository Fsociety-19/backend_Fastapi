from fastapi import APIRouter
from schema.userSchema import *
from schema.appointmentSchema import *
from services.appointment import AppointMent
from Data.models.appointmentModel import AppointMentModel


appointment_router = APIRouter()
@appointment_router.post('/create/appointment', tags=["Appointment"])
def createUser(app:CreateAppointment):
    data=AppointMent.create(AppointMentModel(reason=app.reason,idStudent=app.idStudent,detail=app.detail))
    return data

@appointment_router.get('/get/Appointments', tags=["Appointment"])
def getAll():
    data=AppointMent.getAll()
    return data 

@appointment_router.get('/getTotal/Appointments', tags=["Appointment"])
def getAll():
    data=AppointMent.getCount()
    return data 


@appointment_router.get('/getOne/Appointment', tags=["Appointment"])
def getOne(id:int):
    data=AppointMent.getOne(id)
    return data 


@appointment_router.patch('/update/AppointMent', tags=["Appointment"])
def updateAppointMent(id:int,data:UpdateAppointment):
    data=AppointMent.update(id,AppointMentModel(idStatusAppointment=data.status,idAdminStaff=data.idAdmin,detail=data.detail))
    return data 

@appointment_router.delete('/delete/Appointment', tags=['Appointment'])
def deleteInfo(id:int):
    return AppointMent.delete(id)