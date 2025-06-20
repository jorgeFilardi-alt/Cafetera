"""
PUT / PATCHs
"""
import dal.utils as utils

def proveedor(uId, new_props):
    updated = []
    clause = utils.to_clause(new_props)

    def crud(cursor):
        stmt = f"UPDATE proveedores SET {clause} WHERE id_proveedor = %s"
        cursor.execute(stmt, (uId,))

    # Devolver updated
    def get_updated(cursor):
        query = f"SELECT * FROM proveedores WHERE id_proveedor = %s"
        cursor.execute(query, (uId,))
        return cursor.fetchone()
    
    utils.db_cursor(crud, "WRITE")
    return utils.db_cursor(get_updated, "READ")