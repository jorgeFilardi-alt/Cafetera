from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():

    tmp = random.randint(5,19)

    return {"message": f"Hello World, {tmp}"}