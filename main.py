from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaotest1")
async def funcaoteste():
    return{"teste": "deu certo" }
