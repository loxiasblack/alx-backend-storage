-- script that list all band that has a main style Glam rock
-- and diplay the band and their lifespan
SELECT band_name, (COALESCE(split, 2022) - COALESCE(formed)) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
