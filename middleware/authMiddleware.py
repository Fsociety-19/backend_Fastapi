from fastapi import FastAPI, HTTPException, Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from jwt_manager import createToken, validateToken
from jwt import exceptions
from fastapi.security import HTTPBearer
from starlette.requests import Request
class Authentication(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        auth=await super().__call__(request)
        try:
            return validateToken(auth.credentials)
        except NameError as e:
            raise HTTPException(status_code=403,detail="Sesion no valida")
                     
class AutorizationAdmin(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        auth=await super().__call__(request)
        try:
            info=validateToken(auth.credentials)
            if info['rol']!=1:
                raise HTTPException(status_code=401,detail="Solo para administradores")
        except NameError as e:
            raise Exception(e)
class AutorizationStaf(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        auth=await super().__call__(request)
        try:
            info=validateToken(auth.credentials)
            if info['rol']==2 or info['rol']==1:
                pass
            else:
                raise HTTPException(status_code=401,detail="Solo para administradores")
        except NameError as e:
            raise Exception(e)
                