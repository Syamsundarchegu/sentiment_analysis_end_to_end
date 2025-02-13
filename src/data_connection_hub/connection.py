from src.exception import CustomException
from src.logging import logging
from src.cosntants import *
import pymongo
import pandas as pd


class MongoDBConnection:
    def __init__(self, db_name, collection_name, connection_url):
        self.db_name = db_name
        self.collection_name = collection_name
        self.connection_url = connection_url
    def connecting_monogo_db(self):
        try:
            client = pymongo.MongoClient(self.connection_url)
            db = client[self.db_name]
            collection = db[self.collection_name]
            logging.info("Successfully connected to MongoDB database...")
            return collection.find()
        except Exception as e:
            raise CustomException(f"Failed to connect to MongoDB database. Error: {str(e)}")