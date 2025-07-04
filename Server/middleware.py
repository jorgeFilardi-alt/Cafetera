"""
Middleware - autorizacion con token y manejo de excepciones
contexto, http: refiere a solicitudes no protocolo http/https
"""
import re # Regex
from fastapi import Request # pip install fastapi uvicorn
from fastapi.responses import JSONResponse
from exceptions import InternalException
import dal.auth as auth

# Regex (url path params ej. tecnico/{uId}) (rutas publicas)
API_PUBLIC_PATHS = [
    re.compile(r"^/docs$"),
    re.compile(r"^/login$"),
    re.compile(r"^/register$"),
    re.compile(r"^/tecnicos$"),
    re.compile(r"^/tecnico/\d+$"), # solo numeros
    re.compile(r"^/openapi\.json$")
]

async def access(req: Request, next):
    """
    Access control middleware
    Verifica acceso para toda ruta no publica
    """
    if not any(regex.match(req.url.path) for regex in API_PUBLIC_PATHS):
        token = req.headers.get("Authorization")
        req.state.user = auth.verify(token) # Autenticar con JWT
    return await next(req)

async def exceptions(req: Request, next):
    """
    Traduce excepciones a respuestas http
    Simplifica/Singulariza uso de catchs en el resto funciones
    """
    try:
        return await next(req)
    
    except InternalException as e:
        print(f"[{e.status_code}-{e._origin}] en middleware: {e._msg}")
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