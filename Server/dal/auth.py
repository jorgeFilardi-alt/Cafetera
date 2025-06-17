"""
Autenticacion de usuarios
uso en namespace, auth.user(correo, password)
"""
import os
import jwt
from dotenv import load_dotenv
from datetime import datetime
import dal.utils as utils
from collections import namedtuple
from dataclasses import dataclass
from exceptions import InternalException

load_dotenv()  # Cargar variables de entorno desde .env
User = namedtuple("User", ["correo", "contraseña", "es_administrador"])

@dataclass
class AuthPayload:
    """
    Resultado de autenticación (no autenticado por defecto)
    """
    jwt: str = None
    """Access Token JWT"""
    is_auth: bool = False
    """Credenciales correctas"""
    # Usuario sin contraseña
    es_administrador: bool = False
    correo: str = None


def check_creds(correo, password):
    """
    Verifica credenciales de un usuario - devuelve verdadero o falso
    Dado el usuario en base de datos, verifica si el correo y contraseña coinciden.
    TODO: Computa hash de contraseña y compara con hash almacenado en base de datos.
    """
    # (correo, contraseña, es_administrador)
    query = utils.get_entry("login", "correo", correo)
    if not query or len(query) == 0:
        raise InternalException(f"Usuario: {correo} no existe.", 400, f"Error al autenticar credenciales de {correo}:", "auth.check_creds")
    
    user = User(*query[0])
    if user.contraseña != password:
        raise InternalException(f"Contraseña incorrecta.", 401, f"Error al autenticar credenciales de {correo}:", "auth.check_creds")
    
    # Credenciales correctas, generar JWT
    return True
    
def verify(token):
    """
    Verifica y revalida el token JWT => devuelve su payload
    """
    payload = jwt.decode(token[7:], os.getenv("JWT_SECRET", "jwt_pwd"), algorithms=[os.getenv("JWT_ALGORITHM")])
    latest_user = utils.get_entry("login", "correo", payload.get("correo")) # update payload

    if not latest_user or len(latest_user) == 0:
        raise InternalException(f"Usuario {payload.get("correo")} no existe o jwt desactualizado.", 400, f"Error al autenticar credenciales de {correo}:", "auth.verify")

    if int(payload.get("exp")) < datetime.now().timestamp():
        raise InternalException(f"Token expirado para {payload.get("correo")}.", 401, f"Error al autenticar credenciales de {correo}:", "auth.verify")
    
    user = User(*latest_user[0])
    # Re generar jwt token
    token = gen_jwt(user.correo, user.contraseña)
    
    # Autenticación exitosa
    return AuthPayload(
        jwt=token,
        is_auth=True,
        es_administrador=user.es_administrador,
        correo=user.correo
    )

def gen_jwt(correo, contraseña):
    """
    Genera un token JWT para un usuario.
    Verifica credenciales y genera un token JWT si son correctas.
    Devuelve su payload
    """
    query = utils.get_entry("login", "correo", correo) 
    
    if not query or len(query) == 0:
        raise InternalException(f"Usuario no existe para {correo}.", 400, f"Error al generar token {correo} {contraseña[:2]}", "auth.gen_jwt")
    
    if check_creds(correo, contraseña) is False:
        raise InternalException(f"Credenciales incorrectas para {correo}.", 401, f"Error al generar token {correo} {contraseña[:2]}", "auth.gen_jwt")

    # Generar token para usuario en db
    user = User(*query[0]) 
    payload = {
        "correo": user.correo,
        "es_administrador": user.es_administrador,
        "exp": datetime.now().timestamp() + int(os.getenv("JWT_EXPIRATION", 60 * 60 * 12))
    }

    # Generada Exitosamente
    token = f"Bearer {jwt.encode(payload, os.getenv("JWT_SECRET", "jwt_pwd"), algorithm = os.getenv("JWT_ALGORITHM", "HS256"))}"
    return AuthPayload(
        jwt=token,
        is_auth=True,
        es_administrador=user.es_administrador,
        correo=user.correo
    )