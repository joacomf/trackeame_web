import os
from flask import Flask, render_template
from flask import jsonify
from flask import request, abort
from flask_pymongo import MongoClient


def init(uri=None, db="trackeame"):
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.environ.get("MONGOLAB_URI", uri)
    mongo = MongoClient(uri)
    app.mongo = mongo
    app.database = mongo[db]

    @app.route("/")
    def root_page():
        return render_template("index.html")

    @app.route("/api/users")
    def get_users():
        output = []
        users = app.database.users.find()
        for user in users:
            output.append({"name": user["name"], "lastname": user["lastname"], "sex": user["sex"]})
        return jsonify(output)

    @app.route("/api/users", methods=['POST'])
    def add_user():
        users = app.database.users
        name = request.json["name"]
        lastname = request.json["lastname"]
        sex = request.json["sex"]
        id = users.insert({"name": name, "lastname": lastname, "sex": sex})

        user = users.find_one({'_id': id})
        result = {"name": user["name"], "lastname": user["lastname"], "sex": user["sex"]}

        return jsonify(result)

    @app.route("/api/locations", methods=['DELETE'])
    def clear_locations():
        locations = app.database.locations

        try:
            locations.delete_many({})
        except KeyError:
            abort(403)

        result = {"ok": 1}

        return jsonify(result)

    @app.route("/api/locations", methods=['POST'])
    def add_locations():
        locations = app.database.locations

        try:
            posiciones = request.json["posiciones"]
            posiciones_parseadas = []

            for posicion in posiciones.split("\n"):
                posicion_parseada = posicion.split(",")

                if len(posicion_parseada) == 2:
                    posicion_parseada[0] = float(posicion_parseada[0].replace(" ", ""))
                    posicion_parseada[1] = float(posicion_parseada[1].replace(" ", ""))
                    posiciones_parseadas.append({"posicion": posicion_parseada})

            locations.insert_many(posiciones_parseadas)
        except KeyError:
            abort(403)

        resultado = {"ok": 1}

        return jsonify(resultado)

    @app.route("/api/locations")
    def get_locations():
        output = []
        locations = app.database.locations.find()
        for location in locations:
            output.append({"posicion": location["posicion"]})
        return jsonify(output)

    return app