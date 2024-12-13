import configparser
from pymongo import MongoClient


config = configparser.ConfigParser()
config.read("config/config.ini")
uri = config["MONGODB_CONN"]["conn_str"]

print(uri)

# uri = 'mongodb+srv://' + con_str + '@cluster0.dnzuy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(uri)
db = client["person_records"]
collection = db["person"]


def insert_person(name, age, gender, mobile):
    try:
        person = {
            "name": name,
            "age": age,
            "gender": gender,
            "mobile": mobile
        }
        result = collection.insert_one(person)
        print(f"Person inserted with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error occured: {e}")


# insert_person("vansh", 21, "male", "949596")
# insert_person("vanshika", 21, "female", "94946436")