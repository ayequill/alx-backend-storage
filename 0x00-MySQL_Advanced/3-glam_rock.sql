SELECT
    band_name,
    coalesce(split, '2022-01-01') - formed
        AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam Rock%'
ORDER BY
    lifespan DESC;