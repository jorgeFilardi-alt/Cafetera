"""
Utilidades para la aplicacion de gestion comercial backend
"""

import mysql.connector #pip install mysql-connector-python

DB_USERS = {
    "READ": {"user": "reader", "password": "reader_pass", },
    "WRITE": {"user": "writer", "password": "writer_pass", },
    "ROOT": {"user": "root", "password": "root", },
}

def db_cursor(crud_op, op = "READ"):
    """
    Funcion utilitaria para ejecutar operaciones CRUD
    Simplifica: necesidad de declarar conexion, cursor y close
    """
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="root",
        database='gestion_comercial',
        auth_plugin='mysql_native_password',
        port=3307
    )
    cursor = conexion.cursor()
    try:
        result = crud_op(cursor)
        cursor.close()
        return result
    finally:
        conexion.commit()
        conexion.close()

def san(statement: str | bool | int | None):
    """
    Sanitize Statement - Validar statements SQL (Parameterized) (Custom query builder)
    Simplifica: checkeo de comillas.., caracteres sql injection / argumentos
    nota: remueve tildes, enie.. (cuando %s no posible)
    """
    validChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    sanitized = ''

    if isinstance(statement, (bool, int)) or statement is None:
        return f"{statement}"

    for char in statement.replace(" ", "").replace("\n", "").replace("\t", ""):
        if char in validChars:
            sanitized += char
    return sanitized

def to_clause(data):
    """
    python Dict to  sql SET clause
    """
    return ", ".join(f"{san(key)} = {san(value)}" for key, value in data.items())

def to_tb_cols(model):
    """
    Columns name list (INSERT INTO (__)) (sanitized)
    nombre de columnas a partir de los atributos de un modelo
    """
    atts = list(model.model_fields.keys())
    return ", ".join(f"{san(att)}" for att in atts)

