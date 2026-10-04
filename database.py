import sqlite3


def get_connection():
    return sqlite3.connect("employees.db")


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            knia TEXT NOT NULL,
            maham TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()