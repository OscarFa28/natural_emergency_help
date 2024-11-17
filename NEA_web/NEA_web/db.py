from pymongo import MongoClient
from decouple import config


MONGO_URI = config('MONGO_URI')
MONGO_DB_NAME = config('MONGO_DB_NAME')


client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
