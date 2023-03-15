"""module for configuration our app"""
import os


class Config:
    """describes main config for app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        b'\xe06,e\xc0o\xbf\x03\xeftz\x18\xc7\x03\x94\x82\xa4\x82)9'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:19865421@localhost/items_storage'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __repr__(self):
        return "<class Config>"

    def __str__(self):
        return "<class Config with configuration app>"
