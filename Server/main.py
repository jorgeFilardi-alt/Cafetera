"""
API server - FastAPI (Backend entry point)

uvicorn main:app --reload
"""
from fastapi import FastAPI, Request # pip install fastapi uvicorn
from dataclasses import dataclass, asdict
from exceptions import InternalException
import dal.queries as queries # read?
import dal.crud as crud
import dal.auth as auth
import sql.models as models
import middleware # mdlwr
import helpers

app = FastAPI()

app.middleware("http")(middleware.access)
app.middleware("http")(middleware.exceptions)

@app.get("/clientes")
async def clientes(req: Request):
    return crud.get_table("clientes")

@app.get("/cliente") # singular, ej. GET localhost:8000/cliente?id_cliente=201
async def cliente(id_cliente: str = None, name: str = None, username: str = None):
    return crud.get_entry("clientes", "id_cliente", id_cliente)

@app.get("/proveedores")
async def proveedores(req: Request):
    return crud.get_table("proveedores")

@app.get("/proveedor") # singular, ej. GET localhost:8000/proveedor?id_proveedor=101
async def proveedor(id_proveedor: int = None, name: str = None, username: str = None):
    return crud.get_entry("proveedores", "id_proveedor", id_proveedor)

@app.put("/proveedor") # UPDATE proveedor
async def update_proveedor(req: Request, entry: models.Proveedor):
    # Solo usuarios administradores
    if not req.state.user.es_administrador:
        raise InternalException("Operacion requiere rol de administrador.", 401, f"No admin en {req.path}, {entry}", "PUT:/proveedor")
    
    # Actualizar proveedor
    return crud.update("proveedores", entry)

@app.get("/tecnicos")
async def tecnicos(req: Request):
    return crud.get_table("tecnicos")

@app.get("/tecnico") # singular, ej. GET localhost:8000/tecnico?ci=45556667
async def tecnico(ci: str = None, name: str = None, username: str = None): # TODO: ...params
    return crud.get_entry("tecnicos", "ci", ci)

@app.get("/insumos")
async def insumos(req: Request):
    return crud.get_table("insumos")

@app.get("/insumo") # singular, ej. GET localhost:8000/insumo?id_insumo=1
async def insumo(id_insumo: str = None, name: str = None, username: str = None):
    return crud.get_entry("insumos", "id_insumo", id_insumo)

@app.post("/login")
async def login(req: models.Login):
    payload = auth.gen_jwt(req.correo, req.pwd_hash)
    return payload # Devolver token JWT

@app.post("/register")
async def register(req: Request, entry: models.Login):
    entry = models.Login(correo=entry.correo, pwd_hash=auth.get_creds("", entry.pwd_hash))
    return crud.create("login", entry)
