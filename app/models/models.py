""" Modul for ORM models """

from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String, Float

base = declarative_base()


class Brands(base):
    """ model for brand entity"""
    __tablename__ = 'brands'
    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(String(20), nullable=False)
    country_of_origin = Column(String(20), nullable=False)

    def __repr__(self):
        return f'Class Brand, brand\'s name  is {self.brand_name}'

    def __str__(self):
        return f'Brand is {self.brand_name}'

#
class Items(base):
    """ model for item entity """
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(15), nullable=False)
    item_color = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)
    date_of_production = Column(Date, nullable=False, default=date.today())

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.brand_id'), nullable=False)
    brand_name = db.relationship('Brand', backref=db.backref('brand', lazy=True))

    def __repr__(self):
        return f'Class Item, item\'s name  is {self.item_name}'

    def __str__(self):
        return f'Brand is {self.brand_name}'
