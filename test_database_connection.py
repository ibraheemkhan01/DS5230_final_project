import psycopg2
import getpass
import os
from pathlib import Path

# Check if .env exists
env_file = Path('.env')

if env_file.exists():
    # Load from .env
    from dotenv import load_dotenv
    load_dotenv()
    
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    print("📁 Using credentials from .env file")
else:
    # Prompt for credentials
    print("⚠️ No .env file found. Please enter credentials:")
    DB_HOST = input("DB Host [car-analytics-db.copkksw0o3bx.us-east-1.rds.amazonaws.com]: ") or "car-analytics-db.copkksw0o3bx.us-east-1.rds.amazonaws.com"
    DB_PORT = input("DB Port [5432]: ") or 5432
    DB_NAME = input("Database name [car_analytics_db]: ") or "car_analytics_db"
    DB_USER = input("Username [ds5230_postgres]: ") or "ds5230_postgres"
    password = getpass.getpass("Password: ")
    
    # Ask if they want to save
    save = input("\n💾 Save credentials to .env? (y/n): ").lower()
    if save == 'y':
        with open('.env', 'w') as f:
            f.write(f"DB_HOST={DB_HOST}\n")
            f.write(f"DB_PORT={DB_PORT}\n")
            f.write(f"DB_NAME={DB_NAME}\n")
            f.write(f"DB_USER={DB_USER}\n")
            f.write(f"DB_PASSWORD={password}\n")
        print("✅ Credentials saved to .env (don't commit this file!)")

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
