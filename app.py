from Classes import MongoConnection
from pymongo import MongoClient
from pprint import pprint

_mongoConnection = MongoConnection.MongoConnection.get_instance()
client: MongoClient = _mongoConnection.client
db = client.raspberry1
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
