import pymongo
from Loado.app import config_reader

configuration = config_reader()["DB"]

class Mongo:
    def __init__(self):
        self.host = configuration["host"]
        self.db_name = configuration["db"]
        self.collection_name = configuration["collection"]

    def connect_to_mongodb(self):
        global data_base, IS_CONNECTED
        print(f"hostname is {self.host} and the DB name is {self.db_name}")
        client = pymongo.MongoClient(self.host, 27017)
        data_base = client[self.db_name]
        IS_CONNECTED = True
        return IS_CONNECTED

    def insert_to_mongodb(self, doc = None, **data):
        global collection
        if not IS_CONNECTED:
            self.connect_to_mongodb()
        collection = data_base[self.collection_name]
        if doc:
            collection.insert_one(doc)
            print("Inserted successfully the document")
        else:
            document = {}
            for key in data.keys():
                document[str(key)] = data.get(key)
            collection.insert_one(document)
            print("Inserted successfully the dictionary")

    def get_document(self, value = None, key = None):
        for document in collection.find():
            if value in document.values():
                print(document)
                return document
            elif key in document.keys():
                print(document)
                return document
            else:
                print("Couldn't find a document with the requested values")