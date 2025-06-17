"""
API server - FastAPI (Backend entry point)

uvicorn main:app --reload
"""
from fastapi import FastAPI, Request # pip install fastapi uvicorn
from dataclasses import dataclass
import dal.queries as queries
import dal.utils as utils
import dal.auth as auth
from exceptions import InternalException
from fastapi.responses import JSONResponse

API_PUBLIC_PATHS = ["/login", "/register", "/docs"] # Defecto: todo privado

@dataclass
class LoginBody():
    correo: str = None
    pwd_hash: str = None

app = FastAPI()

@app.middleware("http") # http: refiere a solicitudes no protocolo http/https
async def auth_middleware(req: Request, call_next):
    try:
        if req.url.path not in API_PUBLIC_PATHS:
            token = req.headers.get("Authorization")
            req.state.user = auth.verify(token) # Autenticar con JWT
        return await call_next(req)
    
    except InternalException as e:
        print(f"[{e.status_code}-{e._origin}]: Error Interno: {e._msg}")
        return JSONResponse(
            status_code=e.status_code,
            content=e.detail # _msg info sensible
        )
    
    except Exception as e:
        print(f"Error en middleware: {e}")
        return JSONResponse(
            status_code=500,
            content="Internal Server Error"
        )

@app.get("/clientes")
async def clientes(req: Request):
    return utils.get_table("clientes")

@app.get("/cliente") # singular, ej. GET localhost:8000/cliente?id_cliente=201
async def cliente(id_cliente: str = None, name: str = None, username: str = None):
    return utils.get_entry("clientes", "id_cliente", id_cliente)

@app.get("/proveedores")
async def proveedores(req: Request):
    return utils.get_table("proveedores")

@app.get("/proveedor") # singular, ej. GET localhost:8000/proveedor?id_proveedor=101
async def proveedor(id_proveedor: int = None, name: str = None, username: str = None):
    return utils.get_entry("proveedores", "id_proveedor", id_proveedor)

@app.put("/proveedor") # UPDATE proveedor (solo admin)
async def update_proveedor(req: Request):
    if req.state.user.is_auth and req.state.user.es_administrador:
        print("Privilegios de administrador verificados.")
        return True # TODO: Implementar actualizacion de proveedor
    return False # TODO: Implementar actualizacion de proveedor

@app.get("/tecnicos")
async def tecnicos(req: Request):
    return utils.get_table("tecnicos")

@app.get("/tecnico") # singular, ej. GET localhost:8000/tecnico?ci=45556667
async def tecnico(ci: str = None, name: str = None, username: str = None): # TODO: ...params
    return utils.get_entry("tecnicos", "ci", ci)

@app.get("/insumos")
async def insumos(req: Request):
    return utils.get_table("insumos")

@app.get("/insumo") # singular, ej. GET localhost:8000/insumo?id_insumo=1
async def insumo(id_insumo: str = None, name: str = None, username: str = None):
    return utils.get_entry("insumos", "id_insumo", id_insumo)

@app.post("/login")
async def login(req: LoginBody):
    payload = auth.gen_jwt(req.correo, req.pwd_hash)
    return payload # Devolver token JWT