-- Borrar todas las tablas de la base de datos (orden inverso)
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS mantenimientos;
DROP TABLE IF EXISTS registro_consumo;
DROP TABLE IF EXISTS maquinas;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS tecnicos;
DROP TABLE IF EXISTS insumos;
DROP TABLE IF EXISTS proveedores;
DROP TABLE IF EXISTS login;

SET FOREIGN_KEY_CHECKS = 1;