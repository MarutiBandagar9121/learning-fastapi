from fastapi import FastAPI
from app.controllers.auth.auth_router import router

app= FastAPI()
app.include_router(router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}