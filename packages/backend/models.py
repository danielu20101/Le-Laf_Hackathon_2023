from pydantic import BaseModel, EmailStr, conint


class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str
    role: conint(ge=0, le=2)

class RequestEvent(BaseModel):
    classID: int
    hsAdminID: int
    day: int
    month: int
    year: int

class Student(BaseModel):
    userid: int
    email: str
class AcceptEvent(BaseModel):
    classID: int
    day: int
    month: int
    year: int
    hsAdminID: int
