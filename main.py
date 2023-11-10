from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel
from starlette.requests import Request
from jwt_manager import createToken, validateToken
from fastapi.security import HTTPBearer
from routers.student import student_router
from routers.userRouter import user_router
from routers.appointmentRouer import appointment_router

app=FastAPI()
app.title="AppHub"
app.version="0.0.1"

app.include_router(student_router)
app.include_router(user_router)
app.include_router(appointment_router)


#milldeware
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        auth=await super().__call__(request)
        data=validateToken(auth.credentials)
        raise HTTPException(detail="Hola")
    
@app.get('/token',dependencies=[Depends(JWTBearer)])
def getToken():
    token=createToken(dict(id=1,rol=2))
    return 'token'