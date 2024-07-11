-- write script that sum the table
-- and the nb_fans is selected
SELECT DISTINCT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
