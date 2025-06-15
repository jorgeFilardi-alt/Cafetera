"""
API server using FastAPI (Backend main entry point)

uvicorn main:app --reload
"""
from fastapi import FastAPI # pip install fastapi uvicorn
from dal.queries import get_clientes, get_tecnicos
from dal.utils import get_table, get_entry

app = FastAPI()

@app.get("/clientes")
async def clientes():
    return get_table("clientes")

@app.get("/cliente") # singular, ej. https://localhost:8000/cliente?ci=123456
async def cliente(ci: str = None, name: str = None, username: str = None): # TODO: ...params
    return get_entry("clientes", "ci", ci)

@app.get("/proveedores")
async def proveedores():
    return get_table("proveedores")

@app.get("/tecnicos")
async def tecnicos():
    return get_table("tecnicos")

@app.get("/insumos")
async def insumos():
    return get_table("insumos")