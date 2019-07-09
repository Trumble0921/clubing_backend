from pymongo import MongoClient


class Database(object):

    def __init__(self):
        mongo_domain = "localhost"
        mongo_port = 27017
        self.client = MongoClient(mongo_domain, mongo_port)

    def get_attribute(self, db, collection, *find_keys):
        cursor_collection = self.client[db][collection]
        return cursor_collection.find(find_keys)
