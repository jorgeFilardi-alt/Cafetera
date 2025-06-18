"""
Populate gestion_comercial
python ./sql/populate.py 1
"""
import sys
# ejecucion relativo a dir `./Server`
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from dal.utils import db_cursor

"""
Devolver lista de statments para archivo sql
"""
def get_statements(path: str):
    stmts = []
    with open(path, "r", encoding="utf-8") as f:
        sql_commands = f.read()
    for statement in sql_commands.split(";"):
        stmt = statement.strip()
        # if stmt and not stmt.startswith('--') and not stmt.startswith('/*'):
        stmts.append(stmt)
    return stmts

"""
Ejecutar sql statements en schema.sql & test-data.sql
`override`: 0 = no override, 1 = override, 2 = full reset
"""
def populate(override = 0):
    usrs = get_statements("sql/init.sql")
    rst = get_statements("sql/reset.sql") if int(override) >= 2 else []
    tbs = get_statements("sql/schema.sql") if int(override) >= 1 else []
    pops = get_statements("sql/test-data.sql") 

    def insert(cursor):
        for idx, stmt in enumerate(usrs + rst + tbs + pops):
            print(f"\nPopulate Statement #{idx}:\n\n", stmt)
            cursor.execute(stmt)

    db_cursor(insert, "ROOT")
    print("Database populated successfully.")

if __name__ == "__main__":
    populate(sys.argv[1] if len(sys.argv) > 1 else 0)