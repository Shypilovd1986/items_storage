""" Modul for ORM models """

from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:19865421@localhost/items_storage', echo=True)
Base = declarative_base()


class Brands(Base):
    """ model for brand entity"""
    __tablename__ = 'brands'
    __table_args__ = {'schema': 'items_storage'}
    brand_id = Column(Integer, primary_key=True, unique=True)
    brand_name = Column(String(length=15), nullable=False, unique=True)
    country_of_origin = Column(String(length=15), nullable=False)

    def __repr__(self):
        return f'<Class Brand, brand\'s name  is {self.brand_name}>'

    def __str__(self):
        return f'<Brand is {self.brand_name}>'


class Items(Base):
    """ model for item entity """
    __tablename__ = 'items'
    __table_args__ = {'schema': 'items_storage'}
    item_id = Column(Integer, primary_key=True, unique=True)
    item_name = Column(String(15), nullable=False, unique=True)
    item_color = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)
    date_of_production = Column(Date, nullable=False, default=date.today())
    brand_id = Column(Integer, ForeignKey('items_storage.brands.brand_id'), nullable=False)

    brand_name = relationship('Brands')

    def __repr__(self):
        return f'<Class Item, item\'s name  is {self.item_name}>'

    def __str__(self):
        return f'<Brand is {self.brand_name}>'

Base.metadata.create_all(bind=engine)
