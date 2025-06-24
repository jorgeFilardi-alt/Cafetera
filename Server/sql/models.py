"""
Type safe client schema models
Simplifica uso dentro del programa a traves de tipados @dataclass
Debe: [0] primer elemento ser la primary key (depende en curd.create / update)
TODO: auto-generate script (basade en schema.sql)
"""
from pydantic import BaseModel
from typing import Optional

class Login(BaseModel):
    correo: str
    pwd_hash: str
    es_administrador: Optional[bool] = False

class Proveedor(BaseModel):
    id_proveedor: int
    nombre: Optional[str] = None
    telefono: Optional[int] = None
    en_alta: Optional[bool] = None

class Insumo(BaseModel):
    id_insumo: int
    descripcion: Optional[str] = None
    tipo: Optional[str] = None
    precio_unitario: Optional[int] = None
    id_proveedor: Optional[int] = None

class Cliente(BaseModel):
    id_cliente: int
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[int] = None
    correo: Optional[str] = None

class Maquina(BaseModel):
    id_maquina: int
    modelo: Optional[str] = None
    id_cliente: Optional[int] = None
    direccion_cliente: Optional[str] = None
    costo_alquiler_mensual: Optional[int] = None

class RegistroConsumo(BaseModel):
    id_consumo: int
    id_maquina: int
    id_insumo: int
    fecha: Optional[str] = None  # Puedes usar datetime.date si lo prefieres
    cantidad_usada: Optional[int] = None

class Tecnico(BaseModel):
    ci: int
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[int] = None

class Mantenimiento(BaseModel):
    id_mantenimiento: int
    id_maquina: int
    ci_tecnico: int
    tipo: Optional[str] = None
    fecha: Optional[str] = None  # Puedes usar datetime.date si lo prefieres
    observarciones: Optional[str] = None