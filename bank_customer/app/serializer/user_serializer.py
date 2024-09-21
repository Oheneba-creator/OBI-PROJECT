from pydantic import BaseModel

class UserInSerializer(BaseModel):
    username: str
    password: str
    email: str
    role: str

class UserOutSerializer(BaseModel):
    username: str
    email: str
    role: str
