"""module for configuration our app"""
import os


class Config(object):
    """describes main config for app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe06,e\xc0o\xbf\x03\xeftz\x18\xc7\x03\x94\x82\xa4\x82)9'
