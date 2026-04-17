from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def funcaoteste():
    return{"teste": True "num_aleatorio": random.randint(0,1000)}
