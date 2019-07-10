from pymongo import MongoClient
from bson.objectid import ObjectId


class Database(object):

    def __init__(self):
        mongo_domain = "localhost"
        mongo_port = 27017
        self.client = MongoClient(mongo_domain, mongo_port)

    def get_attribute(self, db, collection, find_options):
        cursor_collection = self.client[db][collection]

        option_list = []
        attribute_list = []

        for find_option_key in find_options.keys():
            if find_options[find_option_key]:
                option_list.append({find_option_key: find_options[find_option_key]})

        for attribute in cursor_collection.find({"$and": option_list}):
            attribute_list.append(attribute)

        return attribute_list

    def insert_attribute(self, db, collection, document):
        cursor_collection = self.client[db][collection]
        cursor_collection.insert(document)


if __name__ == '__main__':
    database_instance = Database()
    database_instance.get_attribute("exercise_db", "exercise_db",
                                    {"$and": [
                                        {"type": "badminton"},
                                        {"member": ObjectId("5d254482b77b79510a30277b")}
                                    ]
                                    }
                                    )
