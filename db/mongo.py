import pymongo

from .store import Store
from ...environment import EnvironmentReader


class Mongo(EnvironmentReader):
    def __init__(self):
        super()
        self.uri = self.get('uri')
        self.user = self.get('user')
        self.password = self.get('password')
        self.database = self.get('database')
        self.collection = self.get('collection')


class MongoStore(Store):
    IDENTIFIER = 'identifier'
    DATA = 'data'

    def __init__(self, client: pymongo.MongoClient, database, collection):
        self.client = client
        self.collection = self.client[database][collection]

    def __query_id(self, identifier):
        return {
            self.IDENTIFIER: identifier
        }

    def save(self, identifier, data):
        document = {
            '$set': {
                self.IDENTIFIER: identifier,
                self.DATA: data,
            }
        }
        query = self.__query_id(identifier)
        self.collection.find_one_and_update(query, document, upsert=True)

    def get(self, identifier):
        query = self.__query_id(identifier)
        document = self.collection.find_one(query)
        return document.get(self.DATA) if document else None
