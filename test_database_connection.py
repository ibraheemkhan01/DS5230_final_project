import psycopg2

# Connection details (replace with your values)
HOST = "car-analytics-db.copkksw0o3bx.us-east-1.rds.amazonaws.com"
PORT = 5432
DATABASE = "car_analytics_db"
USER = "ds5230_postgres"
PASSWORD = "Nu_9nfi3!o12"

try:
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    print("✅ Connected to AWS RDS!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print(f"PostgreSQL version: {cursor.fetchone()[0]}")
    
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")