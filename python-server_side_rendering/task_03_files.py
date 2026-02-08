from flask import Flask, render_template, json, request
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class ProductData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float)

    def __repr__(self):
        return f"{self.id}"

@app.route('/products')
@app.route('/products/<int:id>')
def products(id=None):
    source = request.args.get('source')
    product_list = []

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                product_list = json.load(f).get('products', [])
        except FileNotFoundError:
            pass

    elif source == 'csv':
        try:
            with open('products.csv', mode='r') as f:
                # DictReader returns dictionaries, which match your HTML's .name / .price
                product_list = list(csv.DictReader(f))
        except FileNotFoundError:
            pass

    elif source == 'sql':
        # Querying the SQLite database using SQLAlchemy
        product_list = ProductData.query.all()

    else:
        return 'Wrong source', 400

    # Handle filtering by ID
    if id is not None:
        # Using a list comprehension to keep it as a list for the template loop
        product_list = [p for p in product_list if str(p.get('id') if isinstance(p, dict) else p.id) == str(id)]
        if not product_list:
            return 'Product not found', 404

    return render_template('product_display.html', products=product_list)
if __name__ == '__main__':
    app.run(debug=True, port=5000)