from pydantic import BaseModel, EmailStr


class User(BaseModel):
    login: str
    email: EmailStr
    hashed_password: str
    rating: int

