# Import libraries
import psycopg2
import os

# Database connection settings
db_host = os.getenv("DB_HOST", "db")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("POSTGRES_DB", "products")
db_user = os.getenv("POSTGRES_USER", "postgres")
db_pass = os.getenv("POSTGRES_PASSWORD", "postgres")

# New line to vegetable database
new_vegetable = ("Parsnips", "Fresh", 2.42, 2.19)



try:
    # Connect PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        port=int(db_port), # Cast to int since env vars are strings
        dbname=db_name,
        user=db_user,
        password=db_pass
    )
    cur = conn.cursor()

    # Create vegetable table if it does not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS vegetables (
            id SERIAL PRIMARY KEY,
            name TEXT,
            form TEXT,
            retail_price NUMERIC,
            cup_equivalent_price NUMERIC
        );
    """)

    # Insert row
    cur.execute(
        """
        INSERT INTO vegetables (name, form, retail_price, cup_equivalent_price)
        VALUES (%s, %s, %s, %s);
        """,
        new_vegetable
    )

    # Commit changes
    conn.commit()
    # Close cursor
    cur.close()
    # Close databse connection
    conn.close()
    print(f"ETL complete. 1 row inserted.")

except Exception as e:
    print("Error during ETL:", e)