from fastapi import APIRouter
import hashlib

from ..models.user_model import User
from auth_service_db import client as auth_service_db_client

router_identification = APIRouter()


@router_identification.post("/add")
async def set_user(user: User):
    if user.password != user.confirm_password:
        return_value = {"message": "The password doesn't match"}
    else:
        return_value = await auth_service_db_client.post("/user/add", json={
          "login": user.login,
          "email": user.email,
          "hashed_password": get_password_hash(user.password),
          "rating": 1000
        })
        return_value = return_value.json()
    return return_value


def get_password_hash(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode())
    return hashed_password.hexdigest()


@router_identification.get("/by_login")
async def identification_by_login(login: str, password: str):
    return None


@router_identification.get("/by_email")
async def identification_by_email(email: str, password: str):
    return None
