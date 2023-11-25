from typing import Any
from fastapi import FastAPI
from routers.student import student_router
from routers.userRouter import user_router
from routers.statusRouter import status_router
from routers.appointmentRouer import appointment_router
from routers.auth.login import auth_router
from fastapi.middleware.cors import CORSMiddleware
from middleware.corsMiddleware import cors_config
app=FastAPI()
app.title="AppHub"
app.version="0.0.1"
app.add_middleware(CORSMiddleware,**cors_config)
app.include_router(student_router)
app.include_router(user_router)
app.include_router(appointment_router)
app.include_router(status_router)
app.include_router(auth_router)
