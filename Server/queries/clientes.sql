USE gestion_comercial;

SELECT id_cliente, COUNT(*) AS cantidad_máquinas
FROM máquinas
GROUP BY id_cliente
ORDER BY cantidad_máquinas DESC
LIMIT 5;