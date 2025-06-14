"""
Data access layer for a MySQL database
""" 
import db_cursor from utils

# tabla completa clientes de la empresa
def get_clientes(documento):
    results = []
    def query(cursor):
        query = "SELECT * FROM facturacion.get_clientes WHERE documentocliente = %s"
        cursor.execute(query, (documento,))
        for (id, cliente, fecha, importe) in cursor:
            results.append({"id": id, "cliente": cliente, "fecha": fecha, "importe": importe})

    db_cursor(query)
    return results

if __name__ == "__main__":
    print(get_clientes("123456"))