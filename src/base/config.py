from decouple import config

JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = config('DB_URI')

FLASK_ENV = config('FLASK_ENV', default='production')
FLASK_DEBUG = True
