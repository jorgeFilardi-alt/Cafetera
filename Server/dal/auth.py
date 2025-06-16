"""
Autenticacion de usuarios
uso en namespace, auth.user(correo, password)
"""
import jwt
from datetime import datetime
import dal.utils as utils
from collections import namedtuple

JWT_SECRET = "si_no_si_si"  # Si, va publica porque es un proyecto de faq (TODO: .env)
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION = 60 * 60 * 12 # 12 horas

User = namedtuple("User", ["correo", "contraseña", "es_administrador"])

"""
Verifica credenciales de un usuario - devuelve token, rol, payload
Simplifica: login / generar token
"""
def creds(correo, password):
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
        return {"is_auth": True, 'es_administrador': user.es_administrador, "correo": user.correo, "jwt": _gen_jwt(user.correo)}
    
    # Error
    except Exception as e:
        print(f"Error al autenticar credenciales de {correo}: {e}")
        return {"is_auth": False, 'es_administrador': False, "correo": None, "jwt": None}
    
"""
Verifica y revalida el token JWT => devuelve su payload
"""
def verify(token):
    try:
        payload = jwt.decode(token[7:], JWT_SECRET, algorithms=[JWT_ALGORITHM])
        latest_user = utils.get_entry("login", "correo", payload.get("correo")) # update payload

        if not latest_user or len(latest_user) == 0:
            raise Exception(f"Usuario {payload.get("correo")} no existe o jwt desactualizado.")

        if payload.get("exp") < datetime.now().timestamp():
            raise Exception(f"Token expirado para {payload.get("correo")}.")
        
        user = User(*latest_user[0])
        # Re generar jwt token
        token = _gen_jwt(user.correo)
        
        # Autenticación exitosa
        print(f"Token verificado correctamente para {payload.get("correo")}.")
        return {"is_auth": True, "correo": user.correo, "es_administrador": user.es_administrador, "jwt": token}
    
    except Exception as e:
        print(f"Error al verificar token: {e}")
        return {"is_auth": False, "es_administrador": False, "correo": None, "jwt": None}

"""
@private - Verificar usuario y contraseña de ante mano!
Genera un token JWT para un usuario verificado.
"""
def _gen_jwt(correo):
    try:
        query = utils.get_entry("login", "correo", correo) 
        
        if not query or len(query) == 0:
            raise Exception(f"Usuario no existe para {correo}.")

        # Generar token para usuario en db
        user = User(*query[0]) 
        payload = {
            "correo": user.correo,
            "es_administrador": user.es_administrador,
            "exp": datetime.now().timestamp() + JWT_EXPIRATION
        }

        # Generada Exitosamente
        token = f"Bearer {jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)}"
        print(f"Token generada para {user.correo}.")
        return token
    
    except Exception as e:
        print(f"Error al Generar token: {e}")
        return None