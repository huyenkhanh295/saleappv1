from datetime import datetime

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app import db
import enum


class Roles(enum.Enum):
    ADMIN = 0
    USER = 1


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    creators = relationship('Receipt', backref='receipt_creator', lazy=True)


class Receipt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())
    updated_date = Column(DateTime, default=datetime.now())
    creator_id = Column(Integer, ForeignKey(User.id))
    receipt_detail = relationship('ReceiptDetail', backref='receipt', lazy=True)


class ReceiptDetail(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey(Product.id))
    receipt_id = Column(Integer, ForeignKey(Receipt.id))
    unit_price = Column(Float, default=0)
    quantity = Column(Integer, default=0)


if __name__ == '__main__':
    db.create_all()
