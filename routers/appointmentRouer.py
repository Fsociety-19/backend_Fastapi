from fastapi import APIRouter
from schema.userSchema import *
from schema.appointmentSchema import *
from services.appointment import AppointMent
from Data.models.appointmentModel import AppointMentModel
from fastapi import  Depends
from middleware.authMiddleware import AutorizationAdmin,AutorizationStaf,Authentication

appointment_router = APIRouter()
@appointment_router.post('/create/appointment', tags=["Appointment"], dependencies=[Depends(Authentication())])
def createUser(app:CreateAppointment, id=Depends(Authentication())):
 
    data=AppointMent.create(AppointMentModel(reason=app.reason,idStudent=id['id'],detail=app.detail))
    return 'data'

@appointment_router.get('/get/Appointments', tags=["Appointment"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def getAll():
    data=AppointMent.getAll()
    return data 
@appointment_router.get('/get/AppointmentsbyStaff', tags=["Appointment"],dependencies=[Depends(Authentication()),Depends(AutorizationStaf())])
def getAll(id=Depends(Authentication())):
    data=AppointMent.getbyStaff(id['id'])
    return data 

@appointment_router.get('/getTotal/Appointments', tags=["Appointment"], dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def getAll():
    data=AppointMent.getCount()
    return data 


@appointment_router.get('/getOne/Appointment', tags=["Appointment"],dependencies=[Depends(Authentication()),Depends(AutorizationStaf())])
def getOne(id:int):
    data=AppointMent.getOne(id)
    return data 


@appointment_router.patch('/update/AppointMent', tags=["Appointment"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def updateAppointMent(id:int,data:UpdateAppointment):
    data=AppointMent.update(id,AppointMentModel(idStatusAppointment=data.status,idAdminStaff=data.idAdmin,detail=data.detail))
    return data 

@appointment_router.delete('/delete/Appointment', tags=['Appointment'],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def deleteInfo(id:int):
    return AppointMent.delete(id)