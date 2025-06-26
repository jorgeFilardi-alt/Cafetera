"""
Operaciones CRUD (funciones utilitarias)
"""
import dal.utils as utils

# Create

def create(table: str, full_entry):
    """
    Crear una nuevo registro en tabla
    devuelve el registro creado
    """
    uIdVal = list(full_entry.dict().values())[0]
    uIdCol = list(full_entry.dict().keys())[0]

    def op(cursor):
        cols = utils.to_tb_cols(type(full_entry))
        # parameterized query / prepared statement
        placeholder = ", ".join(["%s"]*len(full_entry.dict()))
        sql = f"INSERT INTO {utils.san(table)} ({cols}) VALUES ({placeholder})"
        cursor.execute(sql, list(full_entry.dict().values()))
    
    utils.db_cursor(op, "WRITE")
    
    # Return affected / modified record row
    return get_entry(table, uIdCol, uIdVal)

# Read

def get_table(table: str):
    """
    Funcion utilitaria, get completo para una tabla (SELECT *)
    Simplifica: endpoints simples, ej. https://localhost:8000/clientes
    """
    results = []
    
    def op(cursor):
        sql = f"SELECT * FROM gestion_comercial.{table}"
        cursor.execute(sql)
        for row in cursor:
            results.append(row)

    utils.db_cursor(op)
    return results

def get_entry(table: str, col: str, value):
    """
    Funcion utilitaria, data point especifico (row / record / entry)
    Dado una tabla, propiedad, y valor
    Simplifica: endpoints individuales simples, ej. https://localhost:8000/cliente/123456
    """
    results = []
    
    def op(cursor):
        sql = f"SELECT * FROM gestion_comercial.{utils.san(table)} WHERE {utils.san(col)} = %s"
        cursor.execute(sql, (value,))
        for row in cursor:
            results.append(row)

    utils.db_cursor(op)
    return results

# Update

def update(table: str, full_entry):
    """
    Para un uId actualizar propiedades
    Devuelve el registro actualizado
    full_entry: contiene None para valores a omitir UPDATE
    """
    uIdVal = list(full_entry.dict().values())[0]
    uIdCol = list(full_entry.dict().keys())[0]    
    clause = utils.to_clause(full_entry.dict(exclude_none = True))

    def op(cursor):
        stmt = f"UPDATE {utils.san(table)} SET {clause} WHERE {utils.san(uIdCol)} = %s"
        cursor.execute(stmt, (uIdVal,))
    
    utils.db_cursor(op, "WRITE")
    
    # Return affected / modified record row
    return get_entry(table, uIdCol, uIdVal)

# Delete