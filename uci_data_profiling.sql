-- How many rows?
SELECT COUNT(*) FROM staging_uci_cars;

-- Check for missing values
SELECT 
    COUNT(*) - COUNT(price) as missing_price,
    COUNT(*) - COUNT(horsepower) as missing_horsepower,
    COUNT(*) - COUNT("normalized-losses") as missing_normalized_losses
FROM staging_uci_cars;

-- What car makes do we have?
SELECT make, COUNT(*) as count
FROM staging_uci_cars
GROUP BY make
ORDER BY count DESC;

-- Price statistics by make
SELECT 
    make,
    COUNT(*) as num_cars,
    ROUND(AVG(price)::numeric, 2) as avg_price,
    MIN(price) as min_price,
    MAX(price) as max_price
FROM staging_uci_cars
WHERE price IS NOT NULL
GROUP BY make
ORDER BY avg_price DESC;

-- Most expensive body styles
SELECT 
    "body-style",
    ROUND(AVG(price)::numeric, 2) as avg_price
FROM staging_uci_cars
WHERE price IS NOT NULL
GROUP BY "body-style"
ORDER BY avg_price DESC;