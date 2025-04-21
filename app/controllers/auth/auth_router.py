from typing import Any
from fastapi import APIRouter
from app.models.request.LoginRequest import LoginRequest
from app.models.response.LoginResponse import LoginResponse

router= APIRouter()

@router.post("/login",response_model=LoginResponse, tags=["auth"])
async def login(req: LoginRequest) -> LoginResponse:
    if req.username == "admin" and req.password == "admin":
        # obj:LoginResponse = LoginResponse()
        # obj.userid = "1234567890"
        # obj.token = "jwtToken"
        # return obj
        return LoginResponse(userid="test_id", token="test_token")