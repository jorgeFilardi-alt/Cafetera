USE gestion_comercial;

SELECT id_cliente, COUNT(*) AS cantidad_maquinas
FROM maquinas
GROUP BY id_cliente
ORDER BY cantidad_maquinas DESC
LIMIT 5;