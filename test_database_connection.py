import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
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
