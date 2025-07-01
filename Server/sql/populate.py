"""
Populate gestion_comercial
python ./sql/populate.py 1
"""
import sys
# ejecucion relativo a dir `./Server`
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
import dal.utils as utils

"""
Ejecutar sql statements en schema.sql & test-data.sql
`override`: 0 = no override, 1 = override, 2 = full reset
"""
def populate(override = 0):
    usrs = utils.get_statements("sql/init.sql")
    rst = utils.get_statements("sql/reset.sql") if int(override) >= 2 else []
    tbs = utils.get_statements("sql/schema.sql") if int(override) >= 1 else []
    pops = utils.get_statements("sql/test-data.sql") 

    def insert(cursor):
        for idx, stmt in enumerate(usrs + rst + tbs + pops):
            print(f"\nPopulate Statement #{idx}:\n\n", stmt)
            cursor.execute(stmt)

    utils.db_cursor(insert, "ROOT")
    print("Database populated successfully.")

if __name__ == "__main__":
    populate(sys.argv[1] if len(sys.argv) > 1 else 0)