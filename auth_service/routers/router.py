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
    response = await auth_service_db_client.get("/user/by_login", params={"user_login": login})
    response = response.json()
    return_message = check_response(response, password)
    return {
        "message": return_message
    }


@router_identification.get("/by_email")
async def identification_by_email(email: str, password: str):
    response = await auth_service_db_client.get("/user/by_email", params={"user_email": email})
    response = response.json()
    return_message = check_response(response, password)
    return {
        "message": return_message
    }


async def identification_by_token():
    pass


def check_response(response: dict, password: str):
    return_message = "Error ;)"
    if ("data" in response) and (len(response["data"]) == 1):
        user_db = response["data"][0]
        if user_db["hashed_password"] == get_password_hash(password):
            return_message = "Correct password"
        else:
            return_message = "Incorrect password"
    elif "message" in response:
        return_message = response["message"]
    return return_message
