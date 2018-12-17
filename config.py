import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    API_ADDRESS = os.environ.get('API_ADDRESS') or 'http://localhost:10000'