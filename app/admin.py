from app import admin, db
from app.models import Category, Product
from flask_admin.contrib.sqla import ModelView


admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))