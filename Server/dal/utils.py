"""
Utilidades para la aplicacion de gestion comercial backend
"""

import mysql.connector #pip install mysql-connector-python

def db_cursor(crud_op):
    """
    Funcion utilitaria para ejecutar operaciones CRUD
    Simplifica: necesidad de declarar conexion, cursor y close
    """
    conexion = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='gestion_comercial',
        auth_plugin='mysql_native_password'
    )
    cursor = conexion.cursor()
    try:
        result = crud_op(cursor)
        cursor.close()
        return result
    finally:
        conexion.commit()
        conexion.close()

def san_stmt(statement: str):
    """
    Sanitize Statement - Validar statements SQL (Parameterized) (Custom query builder)
    Simplifica: checkeo de comillas.., caracteres sql injection
    nota: remueve tildes, enie.. (cuando %s no posible)
    """
    validChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    sanitized = ''
    for char in statement.replace(" ", "").replace("\n", "").replace("\t", ""):
        if char in validChars:
            sanitized += char
    return sanitized

def get_table(table: str):
    """
    Funcion utilitaria, get completo para una tabla (SELECT *)
    Simplifica: endpoints simples, ej. https://localhost:8000/clientes
    """
    results = []
    
    def query(cursor):
        query = f"SELECT * FROM gestion_comercial.{table}"
        cursor.execute(query)
        for row in cursor:
            results.append(row)

    db_cursor(query)
    return results

def get_entry(table: str, property: str, value):
    """
    Funcion utilitaria, data point especifico (row / record / entry)
    Dado una tabla, propiedad, y valor
    Simplifica: endpoints individuales simples, ej. https://localhost:8000/cliente/123456
    """
    results = []
    
    def query(cursor):
        query = f"SELECT * FROM gestion_comercial.{san_stmt(table)} WHERE {san_stmt(property)} = %s"
        cursor.execute(query, (value,))
        for row in cursor:
            results.append(row)

    db_cursor(query)
    return results