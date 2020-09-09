from flask import session

from app import dao, app
from datetime import datetime
import csv
import os


def export_csv():
    products = dao.read_products()
    p = os.path.join(app.root_path, "data/products-%s.csv" % str(datetime.now()))
    with open(p, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "description",
                                               "price", "images", "category_id"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

    return p


def upload_avatar(file):
    path = "images/avatar/" + file.filename
    file.save(os.path.join(app.root_path, "static/", path))

    return path


def add_to_cart(id, name, price):
    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']
    key = str(id)
    if key in cart: # da co sp trong io
        cart[key]["quantity"] = cart[key]["quantity"] + 1
    else: # chua co sp trong io
        cart[key] = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        }

    session["cart"] = cart
    return cart_stats()


def cart_stats():
    q = 0
    s = 0
    if 'cart' in session and session['cart']:
        for item in session["cart"].values():
            q = q + item['quantity']
            s = s + item['quantity'] * item['price']
    return q, s
