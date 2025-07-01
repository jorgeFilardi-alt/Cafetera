USE gestion_comercial;

SELECT ci_tecnico, COUNT(*) AS mantenimientos_realizados
FROM mantenimientos
GROUP BY ci_tecnico
ORDER BY mantenimientos_realizados DESC
LIMIT 5;
