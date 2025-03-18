from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker

from ..models.user_model import User
from ..database.db import engine
from ..database.db_models import User as UserDB

router = APIRouter(prefix="/user")
router_get_only_messages = APIRouter(prefix="/is_exist")

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()


@router.get("/by_id")
async def get_user_by_id(user_id: int):
    return_message = "User doesn't exist"
    user = db.query(UserDB).filter(UserDB.id == user_id).all()
    if len(user):
        return_message = "User exists"
    return {
        "message": return_message,
        "data": user
    }


@router.get("/by_login")
async def get_user_by_login(user_login: str):
    return_message = "User doesn't exist"
    user = db.query(UserDB).filter(UserDB.login == user_login.lower()).all()
    if len(user):
        return_message = "User exists"
    return {
        "message": return_message,
        "data": user
    }


@router.get("/by_email")
async def get_user_by_email(user_email: str):
    return_message = "User doesn't exist"
    user = db.query(UserDB).filter(UserDB.email == user_email.lower()).all()
    if len(user):
        return_message = "User exists"
    return {
        "message": return_message,
        "data": user
    }


@router.post("/add")
async def set_user(user: User):
    # print(f"CALL THE METHOD: set_user(user: User)")
    users_login = db.query(UserDB).filter(UserDB.login == user.login.lower()).all()
    users_email = db.query(UserDB).filter(UserDB.email == user.email.lower()).all()
    if len(users_login):
        return_message = "User login already exists"
    elif len(users_email):
        return_message = "User email already exists"
    else:
        new_user = UserDB(login=user.login.lower(), email=user.email.lower(), nickname=user.login,
                          hashed_password=user.hashed_password, rating=user.rating)
        db.add(new_user)
        db.commit()
        return_message = "User was successfully created"
    return {
        "message": return_message
    }


@router.delete("/by_id")
async def delete_user_by_id(user_id: int):
    return_message = "User doesn't exist"
    user = db.query(UserDB).filter(UserDB.id == user_id).all()
    if len(user) == 1:
        db.delete(*user)
        db.commit()
        return_message = "User was successfully deleted"
    elif len(user) > 1:
        return_message = "ERROR: Count of users more then 1"
    return {
        "message": return_message
    }


@router.delete("/by_login")
async def delete_user_by_login(user_login: str):
    return_message = "User doesn't exist"
    user = db.query(UserDB).filter(UserDB.login == user_login.lower()).all()
    if len(user) == 1:
        db.delete(*user)
        db.commit()
        return_message = "User was successfully deleted"
    elif len(user) > 1:
        return_message = "ERROR: Count of users more then 1"
    return {
        "message": return_message
    }


@router.delete("/by_email")
async def delete_user_by_email(user_email: str):
    return_message = "User doesn't exist"
    user = db.query(UserDB).filter(UserDB.email == user_email.lower()).all()
    if len(user) == 1:
        db.delete(*user)
        db.commit()
        return_message = "User was successfully deleted"
    elif len(user) > 1:
        return_message = "ERROR: Count of users more then 1"
    return {
        "message": return_message
    }


@router_get_only_messages.get("/by_id")
async def is_exist_by_id(user_id: int):
    result = await get_user_by_id(user_id)
    return {
        "message": result["message"]
    }


@router_get_only_messages.get("/by_login")
async def is_exist_by_login(user_login: str):
    result = await get_user_by_login(user_login)
    return {
        "message": result["message"]
    }


@router_get_only_messages.get("/by_email")
async def is_exist_by_email(user_email: str):
    result = await get_user_by_login(user_email)
    return {
        "message": result["message"]
    }



