import json
import os
from app import app
import hashlib
from app.models import Category, Product


def add_user(name, username, password, avatar):
    users = read_user()
    user = {
        "id": len(users) + 1,
        "name": name,
        "avatar": avatar,
        "username": username,
        "password": str(hashlib.md5(password.encode('utf-8')).hexdigest())
    }
    users.append(user)

    return update_json(users, path="data/users.json")


def read_categories():
    return Category.query.all()


def read_product_id(product_id):
    return Product.query.get(product_id)


def read_products(category_id=0, keyword=None, from_price=None, to_price=None, latest=True):
    q = Product.query

    if keyword:
        q = q.filter(Product.name.contains(keyword))

    if from_price and to_price:
        q = q.filter(Product.price__gt__(from_price), Product.price.__lt__(to_price))

    if latest:
        return q.all()[:5]

    return q.all()
    # with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     if category_id > 0:
    #         products = [p for p in products if p["category_id"] == category_id]
    #
    #     if keyword:
    #         products = [p for p in products if p["name"].lower().find(keyword.lower()) >= 0]
    #
    #     if from_price and to_price:
    #         products = [p for p in products if float(from_price) <= p["price"] <= float(to_price)]
    #
    #         # cach truyen thong
    #         # results = []
    #         # for p in products:
    #         #     if p["category_id"] == category_id:
    #         #         results.append()
    #     return products


def update_product(product_id, name, description, price, images, category_id):
    products = read_products()
    for idx, p in enumerate(products):
        if p["id"] == int(product_id):
            products[idx]["name"] = name
            products[idx]["description"] = description
            products[idx]["price"] = float(price)
            products[idx]["images"] = images
            products[idx]["category_id"] = int(category_id)

            break

    return update_json(products)


def update_json(products, path="data/products.json"):
    try:
        with open(os.path.join(app.root_path, path),
                  "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=4)

            return True
    except Exception as ex:
        print(ex)
        return False


def add_product(name, description, price, images, category_id):
    products = read_products()
    product = {
        "id": len(products) + 1,
        "name": name,
        "description": description,
        "price": float(price),
        "images": images,
        "category_id": int(category_id)
    }
    products.append(product)

    try:
        with open(os.path.join(app.root_path, "data/products.json"),
                  "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
            # indent giup format json ngay hang thang loi

            return True
    except Exception as ex:
        print(ex)
        return False


def delete_product(product_id):
    products = read_products()
    # lap tren danh sach, lay chi so dung enumerete do python ho tro
    for idx, product in enumerate(products):
        if product["id"] == int(product_id):
            del products[idx]
            break

    return update_json(products=products)


def read_users():
    with open(os.path.join(app.root_path, "data/users.json"),
              encoding="utf-8") as f:
        return json.load(f)


def add_user(name, username, password, avatar):
    users = read_users()
    user = {
        "id": len(users) + 1,
        "name": name,
        "avatar": avatar,
        "username": username,
        "password": str(hashlib.md5(password.encode('utf-8')).hexdigest())
    }
    users.append(user)

    return update_json(users, path="data/users.json")


def validate_user(username, password):
    users = read_users()
    # strip() tuong tu strim() trong java
    password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())

    for user in users:
        if user["username"].strip() == username.strip() and user["password"] == password:
            return user

    return None


if __name__ == "__main__":
    print(read_products())
