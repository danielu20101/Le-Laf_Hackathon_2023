from pydantic import BaseModel, EmailStr, conint


class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str
    role: conint(ge=0, le=2)