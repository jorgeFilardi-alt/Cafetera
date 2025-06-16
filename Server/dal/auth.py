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

load_dotenv()  # Cargar variables de entorno desde .env
User = namedtuple("User", ["correo", "contraseña", "es_administrador"])

def check_creds(correo, password):
    """
    Verifica credenciales de un usuario - devuelve verdadero o falso
    Dado el usuario en base de datos, verifica si el correo y contraseña coinciden.
    TODO: Computa hash de contraseña y compara con hash almacenado en base de datos.
    """
    try:
        # (correo, contraseña, es_administrador)
        query = utils.get_entry("login", "correo", correo)
        if not query or len(query) == 0:
            raise Exception(f"Usuario: {correo} no existe.")
        
        user = User(*query[0])
        if user.contraseña != password:
            raise Exception(f"Contraseña incorrecta.")
        
        # Credenciales correctas, generar JWT
        print(f"Credenciales correctas para {user.correo}")
        return True
    
    # Error
    except Exception as e:
        print(f"Error al autenticar credenciales de {correo}: {e}")
        return False
    
def verify(token):
    """
    Verifica y revalida el token JWT => devuelve su payload
    """
    try:
        payload = jwt.decode(token[7:], os.getenv("JWT_SECRET", "jwt_pwd"), algorithms=[os.getenv("JWT_ALGORITHM")])
        latest_user = utils.get_entry("login", "correo", payload.get("correo")) # update payload

        if not latest_user or len(latest_user) == 0:
            raise Exception(f"Usuario {payload.get("correo")} no existe o jwt desactualizado.")

        if int(payload.get("exp")) < datetime.now().timestamp():
            raise Exception(f"Token expirado para {payload.get("correo")}.")
        
        user = User(*latest_user[0])
        # Re generar jwt token
        token = gen_jwt(user.correo, user.contraseña)
        
        # Autenticación exitosa
        print(f"Token verificado correctamente para {payload.get("correo")}.")
        return {"is_auth": True, "correo": user.correo, "es_administrador": user.es_administrador, "jwt": token}
    
    except Exception as e:
        print(f"Error al verificar token: {e}")
        return {"is_auth": False, "es_administrador": False, "correo": None, "jwt": None}

def gen_jwt(correo, contraseña):
    """
    Genera un token JWT para un usuario.
    Verifica credenciales y genera un token JWT si son correctas.
    Devuelve su payload
    """
    try:
        query = utils.get_entry("login", "correo", correo) 
        
        if not query or len(query) == 0:
            raise Exception(f"Usuario no existe para {correo}.")
        
        if check_creds(correo, contraseña) is False:
            raise Exception(f"Credenciales incorrectas para {correo}.")

        # Generar token para usuario en db
        user = User(*query[0]) 
        payload = {
            "correo": user.correo,
            "es_administrador": user.es_administrador,
            "exp": datetime.now().timestamp() + int(os.getenv("JWT_EXPIRATION", 60 * 60 * 12))
        }

        # Generada Exitosamente
        token = f"Bearer {jwt.encode(payload, os.getenv("JWT_SECRET", "jwt_pwd"), algorithm = os.getenv("JWT_ALGORITHM", "HS256"))}"
        print(f"Token generada para {user.correo}.")
        return {"is_auth": True, 'es_administrador': user.es_administrador, "correo": user.correo, "jwt": token}
    
    except Exception as e:
        print(f"Error al Generar token: {e}")
        return {"is_auth": False, 'es_administrador': False, "correo": None, "jwt": None}