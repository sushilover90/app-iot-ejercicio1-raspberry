from pymongo import MongoClient


class MongoConnection:
    __instance__ = None
    client: MongoClient = None

    def __init__(self):
        if MongoConnection.__instance__ is None:
            MongoConnection.__instance__ = self
            self.__set_connection()
            return
        raise Exception("There is a MongoConnection class created already")

    @staticmethod
    def get_instance():
        if not MongoConnection.__instance__:
            MongoConnection()

        return MongoConnection.__instance__

    def __set_connection(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017')
