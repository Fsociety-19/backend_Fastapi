from fastapi import APIRouter
from pydantic import BaseModel
from services.auth import Auth
from schema.AuthSchema import AuthShema
from fastapi import FastAPI, HTTPException, Depends
auth_router = APIRouter()
@auth_router.post('/auth/login', tags=["Auth"])
def doLogin(data:AuthShema):
    try:
        return Auth.doLogin(data.username,data.password)
    except Exception as err:
        raise err
