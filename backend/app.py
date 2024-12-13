from flask import Flask, request, jsonify, render_template_string, render_template
import configparser
from pymongo import MongoClient
from bson.objectid import ObjectId
from templates import delete_form_template, person_form_template

app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config/config.ini")
uri = config["MONGODB_CONN"]["conn_str"]

client = MongoClient(uri)
db = client["person_records"]
collection = db["person"]

# Routes

@app.route('/', methods=['GET'])
def hello():
    print("HELLO WORLD")
    return 'hello world'


@app.route('/person/new', methods=['GET'])
def new_person_form():
    return render_template(
        'person_form.html',
        action="Create",
        action_url="/persons",
        person={}
    )



@app.route('/person', methods=['GET'])
def get_people():
    try:
        people_cursor = collection.find({}, {"_id": 1, "name": 1, "age": 1, "gender": 1, "mobile": 1})
        
        people = [{"_id": str(person["_id"]), **person} for person in people_cursor]
        
        return jsonify(people), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch people", "details": str(e)}), 500


@app.route('/persons', methods=['POST'])
def create_person():
    try:
        form_data = request.form.to_dict()

        required_fields = ["name", "age", "gender", "mobile"]
        for field in required_fields:
            if field not in form_data or not form_data[field]:
                return jsonify({"error": f"'{field}' is required"}), 400
        
        try:
            form_data["age"] = int(form_data["age"])
        except ValueError:
            return jsonify({"error": "'age' must be an integer"}), 400

        result = collection.insert_one(form_data)
        
        return jsonify({
            "message": "Person created successfully!",
            "id": str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/person/<id>', methods=['PUT'])
def update_person(id):
    person = collection.find_one({"_id": ObjectId(id)})
    if not person:
        return jsonify({"error": "Person not found"}), 404

    if request.method == "POST" and request.form:
        updated_person = {
            "name": request.form.get("name"),
            "age": int(request.form.get("age")),
            "gender": request.form.get("gender"),
            "mobile": request.form.get("mobile")
        }
        collection.update_one({"_id": ObjectId(id)}, {"$set": updated_person})
        return jsonify({"message": "Person updated successfully!"}), 200

    person["_id"] = str(person["_id"])
    return render_template_string(person_form_template, action="Update", action_url=f"/person/{id}", method="PUT", person=person)

@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
    person = collection.find_one({"_id": ObjectId(id)})
    if not person:
        return jsonify({"error": "Person not found"}), 404

    if request.method == "POST":
        collection.delete_one({"_id": ObjectId(id)})
        return jsonify({"message": "Person deleted successfully!"}), 200

    person["_id"] = str(person["_id"])
    return render_template_string(delete_form_template, person=person, action_url=f"/person/{id}")

if __name__ == '__main__':
    app.run(debug=True)
