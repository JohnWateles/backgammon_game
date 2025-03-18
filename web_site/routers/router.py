from fastapi import APIRouter
from pydantic import BaseModel

from auth_service import client


class User(BaseModel):
    id: int
    name: str


router = APIRouter()


@router.get("/")
async def root():
    response = await client.get("/")
    return {"ROOT": f"ANSWER: {response.json()}"}


@router.get("/login")
async def login():
    return {"LOGIN:": "HTML"}


@router.get("/register")
async def register():
    return {"REGISTER": "HTML"}


@router.post("/register")
async def register_handler_post(user: User):
    print(f"{user.id=}, {user.name=}")
    return {"REGISTER": "HTML"}
