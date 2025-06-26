"""
Utilidades (no especificas a bases de datos)
"""
from pydantic import create_model

def Required(model):
    """
    All fields required
    nota: mas facil con pydantic que con dataclass
    """
    fields = {name: (field.annotation, ...) for name, field in model.model_fields.items()}
    return create_model(f"{model}Required", **fields)

# Not working & unused
# def Optional(model):
#     """
#     Returns a new Pydantic model with all fields optional (by setting default to None).
#     """
#     fields = {name: (field.annotation, None) for name, field in model.model_fields.items()}
#     return create_model(f"{model.__name__}Optional", **fields)