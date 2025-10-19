from pymongo import MongoClient

from config import MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD


def get_db() -> MongoClient:
    return MongoClient("mongodb://schedule_bot-mongo-1", port=27017, username=MONGO_INITDB_ROOT_USERNAME, password=MONGO_INITDB_ROOT_PASSWORD)

mongo = get_db()
