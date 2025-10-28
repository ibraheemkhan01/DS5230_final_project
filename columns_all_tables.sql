-- Columns in staging_uci_cars
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'staging_uci_cars'
ORDER BY ordinal_position;

-- Columns in staging_us_cars
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'staging_us_cars'
ORDER BY ordinal_position;

-- Columns in staging_cardekho
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'staging_cardekho'
ORDER BY ordinal_position;