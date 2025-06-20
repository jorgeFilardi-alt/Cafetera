"""

"""


# ts Required eqvialent fo pydantic
from pydantic import create_model
from sql.models import Proveedor

# All fields required
fields = {name: (field.annotation, ...) for name, field in Proveedor.model_fields.items()}
# ProveedorRequired = create_model("ProveedorRequired", **fields)
def Required():
    return None

