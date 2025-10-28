import psycopg2
import getpass

# Hardcode non-sensitive info
DB_HOST = "car-analytics-db.copkksw0o3bx.us-east-1.rds.amazonaws.com"
DB_PORT = 5432
DB_NAME = "car_analytics_db"
DB_USER = "ds5230_postgres"

# Prompt for password (hidden typing)
password = getpass.getpass("Enter database password: ")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=password
    )
    print("✅ Connected to AWS RDS!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print(f"PostgreSQL version: {version}")
    

    
    cursor = conn.cursor()

    # Create staging table with proper schema
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staging_uci_cars (
        car_id SERIAL PRIMARY KEY,
        make VARCHAR(50) NOT NULL,
        fuel_type VARCHAR(20),
        body_style VARCHAR(30),
        drive_wheels VARCHAR(10),
        aspiration VARCHAR(10),
        engine_location VARCHAR(10),
        engine_type VARCHAR(20),
        fuel_system VARCHAR(20),
        num_of_cylinders VARCHAR(20),
        num_of_doors DECIMAL(3,1),
        wheel_base DECIMAL(6,2),
        length DECIMAL(6,2),
        width DECIMAL(6,2),
        height DECIMAL(6,2),
        bore DECIMAL(5,2),
        stroke DECIMAL(5,2),
        compression_ratio DECIMAL(5,2),
        curb_weight INTEGER,
        engine_size INTEGER,
        city_mpg SMALLINT,
        highway_mpg SMALLINT,
        horsepower DECIMAL(6,2),
        peak_rpm DECIMAL(7,2),
        price DECIMAL(10,2),
        normalized_losses DECIMAL(10,2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Create indexes
    CREATE INDEX idx_aws_staging_make ON staging_uci_cars(make);
    CREATE INDEX idx_aws_staging_price ON staging_uci_cars(price);
    CREATE INDEX idx_aws_staging_body_style ON staging_uci_cars(body_style);
    """)

    conn.commit()
    print("✅ Schema created on AWS RDS!")

    cursor.close()
    conn.close()

    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")