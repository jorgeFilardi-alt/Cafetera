"""
API server using FastAPI (Backend main entry point)

uvicorn main:app --reload
"""
from fastapi import FastAPI # pip install fastapi uvicorn
from dal.queries import get_clientes, get_tecnicos
from dal.utils import get_table
app = FastAPI()

@app.get("/clientes")
async def clientes():
    return get_table("clientes")

@app.get("/proveedores")
async def proveedores():
    return get_table("proveedores")

@app.get("/tecnicos")
async def tecnicos():
    return get_table("tecnicos")

@app.get("/insumos")
async def insumos():
    return get_table("insumos")

# @app.get("/")
# async def root():
#     # smpar = get_clientes("123456")
#     smpar = get_tecnicos("123456")  
#     return {"message": f"Hello World, {2, smpar}"}