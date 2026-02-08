#!/usr/bin/python3
"""
Task 04: Extending Dynamic Data Display to Include SQLite in Flask
"""

import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")
DB_PATH = os.path.join(BASE_DIR, "products.db")


def read_products_json(filepath):
    """Read products from JSON file and return list of dicts."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    products = []
    for item in data:
        products.append({
            "id": int(item.get("id")),
            "name": item.get("name"),
            "category": item.get("category"),
            "price": float(item.get("price")),
        })
    return products


def read_products_csv(filepath):
    """Read products from CSV file and return list of dicts (robust)."""
    products = []

    # utf-8-sig removes BOM if present (common on Windows)
    with open(filepath, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Skip completely empty/bad rows
            if not row or row.get("id") in (None, "", " "):
                continue

            products.append({
                "id": int(row["id"]),
                "name": row.get("name", "").strip(),
                "category": row.get("category", "").strip(),
                "price": float(row["price"]),
            })

    return products


def read_products_sql(db_path):
    """Read products from SQLite DB and return list of dicts."""
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for r in rows:
        products.append({
            "id": int(r["id"]),
            "name": r["name"],
            "category": r["category"],
            "price": float(r["price"]),
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    error = None
    product_list = []

    # Load from correct source
    try:
        if source == "json":
            product_list = read_products_json(JSON_PATH)
        elif source == "csv":
            product_list = read_products_csv(CSV_PATH)
        elif source == "sql":
            product_list = read_products_sql(DB_PATH)
        else:
            error = "Wrong source"
            return render_template("product_display.html", products=[], error=error)
    except sqlite3.Error:
        error = "Database error"
        return render_template("product_display.html", products=[], error=error)
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        # Covers missing/corrupted JSON/CSV or bad conversions
        error = "Data source error"
        return render_template("product_display.html", products=[], error=error)

    # Optional filter by id
    if product_id is not None:
        try:
            pid = int(product_id)
        except ValueError:
            error = "Product not found"
            return render_template("product_display.html", products=[], error=error)

        filtered = [p for p in product_list if p["id"] == pid]
        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", products=[], error=error)

        product_list = filtered

    return render_template("product_display.html", products=product_list, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
