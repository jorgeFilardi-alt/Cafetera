"""
Data access layer for a MySQL database
""" 
import mysql.connector #pip install mysql-connector-python

def facturas(documento):
    conexion = mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='gestion_comercial',auth_plugin='mysql_native_password')
    cursor = conexion.cursor()

    query = "select * from facturacion.facturas where documentocliente = '{}'".format(documento)
    print(query)
    cursor.execute(query)
    for (id,cliente,fecha,importe) in cursor:
        print("Cliente: {} - Fecha: {} - Importe: {}".format(cliente,fecha,importe))

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    facturas("123456")