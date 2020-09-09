from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
app = Flask(__name__)
app.secret_key = "[\xdd\xa5\xfb\x85\x1c\x1d\xf2\x8d\x196ms\x02-\x17"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/saledb01?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

admin = Admin(app=app)
db = SQLAlchemy(app=app)