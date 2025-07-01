USE gestion_comercial;

SELECT ci_técnico, COUNT(*) AS mantenimientos_realizados
FROM mantenimientos
GROUP BY ci_técnico
ORDER BY mantenimientos_realizados DESC
LIMIT 5;
