from app import dao, app
from flask import session
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


def upload_avatar(f):
    p = 'images/avatar/%s' % f.filename
    f.save(os.path.join(app.root_path, "static/", p))

    return p


def add_to_cart(product_id, name, price):
    if "cart" not in session:
        session["cart"] = {}

    cart = session["cart"]
    key = str(product_id)
    if key in cart:
        cart[key]["quantity"] = cart[key]["quantity"] + 1
    else:
        cart[key] = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": 1
        }

    session["cart"] = cart
