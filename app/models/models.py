""" Modul for ORM models """

from datetime import datetime
from app import db


class Brand(db.Model):
    """ model for brand entity"""
    __tablename__ = 'brand'
    brand_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(20), nullable=False)
    country_of_origin = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Class Brand, brand\'s name  is {self.brand_name}'

    def __str__(self):
        return f'Brand is {self.brand_name}'


class Item(db.Model):
    """ model for item entity """
    __tablename__ = 'item'
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(20), nullable=False)
    item_color = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_of_production = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.brand_id'), nullable=False)
    brand_name = db.relationship('Brand', backref=db.backref('brand', lazy=True))

    def __repr__(self):
        return f'Class Item, item\'s name  is {self.item_name}'

    def __str__(self):
        return f'Brand is {self.brand_name}'
