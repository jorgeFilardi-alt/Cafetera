USE gestion_comercial;

SELECT i.id_insumo, i.precio_unitario, SUM(c.cantidad_usada) AS consumo
FROM insumos i
JOIN registro_consumo c ON i.id_insumo = c.id_insumo
GROUP BY i.id_insumo
ORDER BY i.precio_unitario DESC, consumo DESC
LIMIT 5;