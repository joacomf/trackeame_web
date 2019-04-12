import os
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGOLAB_URI", None)
mongo = PyMongo(app)

@app.route("/")
def getUsers():
    output = []
    users = mongo.db.users.find()
    for user in users:
        output.append({"name": user["name"], "lastname": user["lastname"], "sex": user["sex"]})
    return jsonify(output)

@app.route("/", methods=['POST'])
def addUser():
    users = mongo.db.users
    name = request.json["name"]
    lastname = request.json["lastname"]
    sex = request.json["sex"]
    id = users.insert({"name": name, "lastname": lastname, "sex": sex})

    user = users.find_one({'_id': id})
    result = {"name": user["name"], "lastname": user["lastname"], "sex": user["sex"]}

    return jsonify(result)