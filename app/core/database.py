import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

# Load .env variables (use only in dev; use a config system for prod)
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")


if not MONGO_URI or not MONGO_DB_NAME:
    raise Exception("MONGO_URI or MONGO_DB_NAME is not set in the environment.")

# Initialize MongoDB client
client = MongoClient(MONGO_URI)

# Reference to the specific database
db: Database = client[MONGO_DB_NAME]


def get_db() -> Database:
    """
    Returns the MongoDB database instance.
    """
    return db


def get_collection(name: str) -> Collection:
    """
    Helper to get a collection by name.
    """
    return db[name]
