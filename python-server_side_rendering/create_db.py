#!/usr/bin/python3
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "products.db")

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cur.execute("DELETE FROM Products")

    cur.executemany(
        "INSERT INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
        [
            (1, "Laptop", "Electronics", 799.99),
            (2, "Coffee Mug", "Home Goods", 15.99),
        ],
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created:", DB_PATH)
