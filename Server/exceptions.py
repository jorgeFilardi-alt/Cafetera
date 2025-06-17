"""
Excepciones personalizadas para el servidor.
Abstraccion principal: manejo de respuestas HTTP y errores (con sin exponer detalles sensibles).
"""
# from fastapi import HTTPException

class InternalException(Exception):
    """
    Raised en internal server errors.
    """
    def __init__(self, msg, status_code, internalMsg = None, internalOrigin = "Uknown"):
        self._msg = internalMsg if internalMsg else msg
        self._origin = internalOrigin
        self.status_code = status_code
        self.detail = msg
        super().__init__(msg)

"""
HTTPException - de fastapi

status_code: El código de estado HTTP (por ejemplo, 401, 404, 400, etc.).
detail: Un mensaje o descripción del error.
"""