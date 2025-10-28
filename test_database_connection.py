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
    
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
