import os
import psycopg


def get_connection():
    return psycopg.connect(os.environ["DATABASE_URL"])


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            nom TEXT NOT NULL,
            knia TEXT NOT NULL,
            maham TEXT NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()
