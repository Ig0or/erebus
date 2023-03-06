# Third Party
from decouple import config
from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDBInfrastructure:
    __connection = None

    @staticmethod
    def __create_client() -> MongoClient:
        host = config("MONGO_HOST")
        client = MongoClient(host=host)

        return client

    @classmethod
    def __create_connection(cls) -> Collection:
        database_name = config("MONGO_DATABASE")
        collection_name = config("MONGO_COLLECTION")

        client = cls.__create_client()
        db_connection = client[database_name]
        collection = db_connection[collection_name]

        return collection

    @classmethod
    def get_connection(cls) -> Collection:
        if cls.__connection is None:
            cls.__connection = cls.__create_connection()

        return cls.__connection
