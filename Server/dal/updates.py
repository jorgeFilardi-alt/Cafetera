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

    #TODO: devolver updated
    return utils.db_cursor(crud, "WRITE")