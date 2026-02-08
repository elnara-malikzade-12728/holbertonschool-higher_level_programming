from flask import Flask, render_template, json, request
from flask_sqlalchemy import SQLAlchemy
import csv
import os
import json

app = Flask(__name__)
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class ProductData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float)

# Root route to prevent 404 Not Found error
@app.route('/')
def home():
    return "<h1>Welcome to the Product API</h1><p>Use /products?source=json to see data.</p>"

@app.route('/products')
@app.route('/products/<int:id>')
def products(id=None):
    # Fetch source from URL: /products?source=json
    source = request.args.get('source')
    
    if not source:
        return 'Wrong source', 400

    product_list = []

    # 1. Handle JSON Source
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                data = json.load(f)
                # If data is a dictionary, extract the 'products' list
                if isinstance(data, dict):
                    product_list = data.get('products', [])
                # If data is already a list, use it directly
                elif isinstance(data, list):
                    product_list = data
        except (FileNotFoundError, json.JSONDecodeError):
            product_list = []

    # 2. Handle CSV Source
    elif source == 'csv':
        try:
            with open('products.csv', mode='r') as f:
                product_list = list(csv.DictReader(f))
        except FileNotFoundError:
            product_list = []

    # 3. Handle SQL Source
    elif source == 'sql':
        product_list = ProductData.query.all()

    else:
        return 'Wrong source', 400

    # Handle optional filtering by ID
    if id is not None:
        filtered = []
        for p in product_list:
            # Check ID for both dicts (JSON/CSV) and objects (SQL)
            p_id = p.get('id') if isinstance(p, dict) else p.id
            if str(p_id) == str(id):
                filtered.append(p)
        
        if not filtered:
            return 'Product not found', 404
        product_list = filtered

    return render_template('product_display.html', products=product_list)

if __name__ == '__main__':
    # Initialize the database automatically
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)