from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "name": "FastAPI",
    }

@app.get("/maruti")
async def maruti():
    return {
        "message": "Hello World",
        "name": "Maruti",
    }

# app.run(debug=True)