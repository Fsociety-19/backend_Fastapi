from fastapi import APIRouter
from pydantic import BaseModel
from schema.userSchema import *
from services.users import User
from Data.models.userdetailModel import UserDetailModel
from fastapi import FastAPI, Depends
from middleware.authMiddleware import AutorizationAdmin,AutorizationStaf,Authentication

user_router = APIRouter()
@user_router.post('/create/user', tags=["users"])
def createUser(user:CreateUser):
    data=User.create(user)
    return data

@user_router.get('/get/users', tags=["users"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def getAll():
    data=User.getAll()
    return data
@user_router.get('/get/usersdetail', tags=["users"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def getAll():
    data=User.getAllDetail()
    return data  
@user_router.get('/getOne/user', tags=["users"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def getOne(id:int):
    data=User.getOne(id)
    return data 
@user_router.get('/get/Admins', tags=["users"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def getOne():
    data=User.getAdmins()
    return data 

@user_router.get('/findOne/user', tags=["users"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def findOne(name:str):
    data=User.findOne(name)
    return data 

@user_router.patch('/update/userDetail', tags=["users"],dependencies=[Depends(Authentication()),Depends(AutorizationAdmin())])
def updateUser(data:updateUserDetail):
    data=User.update(id,UserDetailModel(dni=data.dni,name=data.name,lastName=data.lastName,idUser=data.idUser))
    return data 

@user_router.delete('/delete/userDetail', tags=['users'])
def deleteInfo(id:int):
    return User.deleteUserDetail(id)

@user_router.delete('/delete/userDetailByName', tags=['users'])
def deleteInfo(id:int):
    return User.deleteUserDetail(id)