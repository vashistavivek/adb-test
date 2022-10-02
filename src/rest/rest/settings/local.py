from rest.settings.base import *
from pymongo import MongoClient

MONGO_DB = 'test_db'
MONGO_URI = 'mongodb://' + env.get("MONGO_HOST") + ':' + env.get("MONGO_PORT")
MONGO_DATABASE = MongoClient(MONGO_URI)[MONGO_DB]