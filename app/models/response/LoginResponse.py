from pydantic import BaseModel

class LoginResponse(BaseModel):
    userid: str
    token: str