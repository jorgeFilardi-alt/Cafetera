"""
API server - FastAPI (Backend entry point)

uvicorn main:app --reload
"""
from fastapi import FastAPI # pip install fastapi uvicorn
from dal.queries import get_clientes, get_tecnicos
from dal.utils import get_table, get_entry
import dal.auth as auth

app = FastAPI()

@app.get("/clientes")
async def clientes():
    auth.user("admin@gc.com", "adminpass123")
    return get_table("clientes")

@app.get("/cliente") # singular, ej. GET localhost:8000/cliente?id_cliente=201
async def cliente(id_cliente: str = None, name: str = None, username: str = None):
    return get_entry("clientes", "id_cliente", id_cliente)

@app.get("/proveedores")
async def proveedores():
    return get_table("proveedores")

@app.get("/proveedor") # singular, ej. GET localhost:8000/proveedor?id_proveedor=101
async def proveedor(id_proveedor: int = None, name: str = None, username: str = None):
    return get_entry("proveedores", "id_proveedor", id_proveedor)

@app.get("/tecnicos")
async def tecnicos():
    return get_table("tecnicos")

@app.get("/tecnico") # singular, ej. GET localhost:8000/tecnico?ci=45556667
async def tecnico(ci: str = None, name: str = None, username: str = None): # TODO: ...params
    return get_entry("tecnicos", "ci", ci)

@app.get("/insumos")
async def insumos():
    return get_table("insumos")

@app.get("/insumo") # singular, ej. GET localhost:8000/insumo?id_insumo=1
async def insumo(id_insumo: str = None, name: str = None, username: str = None):
    return get_entry("insumos", "id_insumo", id_insumo)