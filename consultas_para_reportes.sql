USE Obligatorio;

SELECT m.id_cliente, SUM(m.costo_alquiler_mensual + c.cantidad_usada*i.precio_unitario) AS total_a_cobrar
FROM máquinas m
JOIN registro_consumo c ON m.id_máquina = c.id_máquina
JOIN insumos i ON c.id_insumo = i.id_insumo
WHERE YEAR(c.fecha) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH) AND MONTH(c.fecha) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)
GROUP BY m.id_cliente
ORDER BY m.id_cliente;

SELECT i.id_insumo, i.precio_unitario, SUM(c.cantidad_usada) AS consumo
FROM insumos i
JOIN registro_consumo c ON i.id_insumo = c.id_insumo
GROUP BY i.id_insumo
ORDER BY i.precio_unitario DESC, consumo DESC
LIMIT 5;

SELECT ci_técnico, COUNT(*) AS mantenimientos_realizados
FROM mantenimientos
GROUP BY ci_técnico
ORDER BY mantenimientos_realizados DESC
LIMIT 5;

SELECT id_cliente, COUNT(*) AS cantidad_máquinas
FROM máquinas
GROUP BY id_cliente
ORDER BY cantidad_máquinas DESC
LIMIT 5;