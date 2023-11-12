from pydantic import BaseModel, EmailStr, conint


class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str
    role: conint(ge=0, le=2)

class RequestEvent(BaseModel):
    email: str
    password: str
    day: int
    month: int
    year: int
