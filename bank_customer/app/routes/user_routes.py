from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.database import db_session
from app.serializer.user_serializer import UserInSerializer
from app.controller.user_controller import add_user, signin


user_router = APIRouter()

@user_router.post("/admin/users/add")
async def create_user(data: UserInSerializer, db=Depends(db_session)):
    new_user = await add_user(db, data)
    if new_user.data:
        return new_user
    
@user_router.post("/login")
def login_user(prosp_username, prosp_password, db=Depends(db_session)):
    if prosp_username and prosp_password:
        signin_process = signin(db, 
                                {"username": prosp_username, "password": prosp_password})
        return signin_process