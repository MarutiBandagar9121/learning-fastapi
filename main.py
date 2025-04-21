from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

class ProductStatus(str,Enum):
    PENDING="PENDING",
    IN_PROGRESS="IN_PROGRESS",
    COMPLETED="COMPLETED",
    FAILED="FAILED"

class RegistrationRequest(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:str
    password:str

app = FastAPI()

#sending list and object in response
@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "name": "FastAPI",
        "values": [1, 2, 3, 4, 5],
        "object": {
            "name": "FastAPI",
            "version": 0.1,
            "author": "John Doe",
        },
    }

@app.get("/home")
async def home():
    return {
        "message": "Hello World",
        "name": "home",
    }

@app.get("/aboutus")
async def aboutus():
    return {
        "message": "Hello World",
        "name": "aboutus",
    }

#passing parameter
@app.get("/items/{item_id}")
async def read_item(item_id:str):
    return {"item_id": item_id}


@app.get("/status/{status}")
async def status_check(status: ProductStatus):
    if(status.value == "PENDING"):
        return {"status": "Pending"}
    elif(status.value == "IN_PROGRESS"):
        return {"status": "In Progress"}
    elif(status.value == "COMPLETED"):
        return {"status": "Completed"}
    elif(status.value == "FAILED"):
        return {"status": "Failed"}
    
@app.get("/files/{filepath:path}")
async def getFile(filepath:str):
    return {"path":filepath}

#path parameters
@app.get("/query")
async def queryParam(status:int=0,name:str=""):
    return {"status":status,"name":name}


# with request body
@app.post("/register")
async def register_user(request:RegistrationRequest):
    return {
        "username": request.username,
        "email": request.email,
    }

# query params and string validation
@app.get("/queryparams")
async def query_params(name:Annotated[str | None,Query(min_length=3,max_length=10)]=None):
    return {"name": name}

@app.get("/approveemail")
async def approve_email(email: Annotated[str | None, Query(min_length=8, pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")]=None):
    if email is not None:
        return {
            "message": "Email approved",
            "status": True,
        }
    else:
        return{
            "message": "Email not approved",
            "status": False,
        }