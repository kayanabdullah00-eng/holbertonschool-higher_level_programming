from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))


def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT id, name, category, price FROM Products'
    )

    rows = cursor.fetchall()

    products = []

    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })

    conn.close()

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json()

    elif source == 'csv':
        products = read_csv()

    elif source == 'sql':
        products = read_sql()

    else:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    if product_id:
        filtered_products = [
            product for product in products
            if str(product['id']) == product_id
        ]

        if not filtered_products:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

        products = filtered_products

    return render_template(
        'product_display.html',
        products=products,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
