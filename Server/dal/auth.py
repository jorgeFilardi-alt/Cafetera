"""
Autenticacion de usuarios
uso en namespace, auth.user(correo, password)
"""
import dal.utils as utils

"""
Autentica un usuario y devuelve su rol
Retorna True si las credenciales son correctas, False en caso contrario.
"""
def user(correo, password):
    try:
        # (correo, contraseña, es_administrador)
        query = utils.get_entry("login", "correo", correo)
        if not query:
            print(f"email o pwd incorrectas para {correo}.") # Usuario no existe
            return False
        
        user = query[0]
        # Credenciales correctas
        if user[1] == password:
            print(f"Usuario {correo} autenticado correctamente.", user[0])
            return {'admin': user[2]}
        else:
            print(f"email o pwd incorrectas para {correo}.") # Contraseña incorrecta
            return False
    
    # Error
    except Exception as e:
        print(f"Error al autenticar usuario {correo}: {e}")
        return False
    