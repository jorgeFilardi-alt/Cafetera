"""
API server using FastAPI

uvicorn main:app --reload
"""
from fastapi import FastAPI # pip install fastapi uvicorn
from dal import get_clientes, get_tecnicos
app = FastAPI()

@app.get("/")
async def root():
    # smpar = get_clientes("123456")
    smpar = get_tecnicos("123456")  
    return {"message": f"Hello World, {2, smpar}"}