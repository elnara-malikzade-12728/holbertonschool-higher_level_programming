#!/usr/bin/python3
"""
Task 03: Displaying Data from JSON or CSV Files in Flask
"""

import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")


def read_products_json(filepath):
    """Read products from a JSON file and return a list of dicts."""
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
    """Read products from a CSV file and return a list of dicts."""
    products = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row.get("id")),
                "name": row.get("name"),
                "category": row.get("category"),
                "price": float(row.get("price")),
            })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    error = None
    product_list = []

    if source == "json":
        product_list = read_products_json(JSON_PATH)
    elif source == "csv":
        product_list = read_products_csv(CSV_PATH)
    else:
        error = "Wrong source"
        return render_template("product_display.html", products=[], error=error)

    # Optional filtering by id
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
