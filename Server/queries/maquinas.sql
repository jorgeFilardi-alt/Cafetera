USE gestion_comercial;

SELECT m.id_cliente, SUM(m.costo_alquiler_mensual + c.cantidad_usada*i.precio_unitario) AS total_a_cobrar
FROM máquinas m
JOIN registro_consumo c ON m.id_máquina = c.id_máquina
JOIN insumos i ON c.id_insumo = i.id_insumo
WHERE YEAR(c.fecha) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH) AND MONTH(c.fecha) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)
GROUP BY m.id_cliente
ORDER BY m.id_cliente;