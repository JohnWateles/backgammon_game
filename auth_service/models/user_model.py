from pydantic import BaseModel, EmailStr


class User(BaseModel):
    login: str
    email: EmailStr
    password: str
    confirm_password: str
