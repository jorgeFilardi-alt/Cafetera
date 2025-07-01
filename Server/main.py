"""
API server - FastAPI (Backend entry point)
Estructura de api: `./Consigna.pdf`
"""
from fastapi import FastAPI, Request # type: ignore

from exceptions import InternalException
import openapi as custom_openapi
import middleware # mdlwr

import sql.models as models # tipado del schema
import dal.auth as auth # autenticacion
import dal.crud as crud # SQL ops

app = FastAPI()
# /docs -H Authorization (button)
app.openapi = lambda: custom_openapi.custom(app)
app.middleware("http")(middleware.access)
app.middleware("http")(middleware.exceptions)

# Autenticacion y usuarios

@app.post("/login")
async def login(req: models.Login):
    payload = auth.gen_jwt(req.correo, req.pwd_hash)
    return payload # Devolver token JWT

@app.post("/register")
async def register(_, entry: models.Login):
    entry = models.Login(correo=entry.correo, pwd_hash=auth.get_creds("", entry.pwd_hash))
    return crud.create("login", entry)

# 1. ABM, Alta baja y modificacion

@app.put("/proveedor") # UPDATE proveedor
async def update_proveedor(req: Request, entry: models.Proveedor):
    # Solo usuarios administradores
    if not req.state.user.es_administrador:
        raise InternalException("Operacion requiere rol de administrador.", 401, f"No admin en {req.path}, {entry}", "PUT:/proveedor")
    
    # Actualizar proveedor
    return crud.update("proveedores", entry)

# 5. Consultas para reportes

@app.get("/reporte-clientes")
async def reporte_clientes():
    """
    Reporte 5.1: total mensual a cobrar a cada cliente
    suma alquileres de maquinas mas costo insumos cosnumidos
    """
    return crud.sql_file("queries/clientes")

@app.get("/reporte-consumos")
async def reporte_consumos():
    """
    Reporte 5.2: consumo de insumos con precio
    """
    return crud.sql_file("queries/consumos")

@app.get("/reporte-mantenimientos")
async def reporte_mantenimientos():
    """
    Reporte 5.3: tecnicos con mas mantenimientos
    """
    return crud.sql_file("queries/mantenimientos")

@app.get("/reporte-maquinas")
async def reporte_maquinas():
    """
    Reporte 5.4: clientes con mas maquinas
    """
    return crud.sql_file("queries/maquinas")

# SQL Table endpoints

@app.get("/clientes")
async def clientes():
    return crud.get_table("clientes")

@app.get("/proveedores")
async def proveedores():
    return crud.get_table("proveedores")

@app.get("/tecnicos")
async def tecnicos():
    return crud.get_table("tecnicos")

@app.get("/insumos")
async def insumos():
    return crud.get_table("insumos")

# SQL Entry endpoints

@app.get("/cliente/{uId}") # singular, ej. GET localhost:8000/cliente?id_cliente=201
async def cliente(uId: int | str):
    return crud.get_entry("clientes", "id_cliente", uId)

@app.get("/proveedor/{uId}") # singular, ej. GET localhost:8000/proveedor?id_proveedor=101
async def proveedor(uId: int | str):
    return crud.get_entry("proveedores", "id_proveedor", uId)

@app.get("/tecnico/{uId}") # singular, ej. GET localhost:8000/tecnico?ci=45556667
async def tecnico(uId: int | str):
    return crud.get_entry("tecnicos", "ci", uId)

@app.get("/insumo/{uId}") # singular, ej. GET localhost:8000/insumo?id_insumo=1
async def insumo(uId: int | str):
    return crud.get_entry("insumos", "id_insumo", uId)