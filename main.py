from fastapi import FastAPI
from enum import Enum

class ProductStatus(str,Enum):
    PENDING="PENDING",
    IN_PROGRESS="IN_PROGRESS",
    COMPLETED="COMPLETED",
    FAILED="FAILED"

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


@app.get("/query")
async def queryParam(status:int=0,name:str=""):
    return {"status":status,"name":name}