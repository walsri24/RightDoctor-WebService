from pymongo import MongoClient
import configparser


config = configparser.ConfigParser()
config.read("config/config.ini")
con_str = config["MONGODB_CONN"]["conn_str"]


uri = 'mongodb+srv://' + con_str + '@cluster0.dnzuy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(uri)
db = client["person_records"]
collection = db["person"]

print(db)