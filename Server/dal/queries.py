"""
Data Access Layer (MySQL database)
""" 
import dal.utils as utils

def gen_data():
    return "ad"


# tabla completa clientes de la empresa
def get_clientes(documento):
    results = []
    def query(cursor):
        query = "SELECT * FROM gestion_comercial.clientes" # WHERE documentocliente = %s
        cursor.execute(query, (documento,))
        for (id_cliente, nombre, direccion) in cursor:
            results.append({"id_cliente": id_cliente, "nombre": nombre, "direccion": direccion})

    utils.db_cursor(query)
    return results

# TODO: use full query for SELECT *
# tabla completa clientes de la empresa
def get_tecnicos():
    results = []
    def query(cursor):
        query = "SELECT * FROM gestion_comercial.tecnicos" # WHERE documentocliente = %s
        cursor.execute(query)
        print(cursor)
        for (ci, nombre, apellido, telefono) in cursor:
            results.append({"ci": ci, "nombre": nombre, "telefono": telefono})

    utils.db_cursor(query)
    return results