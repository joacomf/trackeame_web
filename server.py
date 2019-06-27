import os
from flask import Flask, render_template
from flask import jsonify
from flask import request, abort
from flask_pymongo import MongoClient

from datetime import datetime

def init(uri=None, db="trackeame"):
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.environ.get("MONGOLAB_URI", uri)
    mongo = MongoClient(app.config["MONGO_URI"])
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

        cuadrantes = {"N": 1, "S":-1, "W":-1, "E": 1}

        try:
            posiciones = request.json["posiciones"]
            posiciones_parseadas = []
            ultima_posicion = None

            for posicion in posiciones.split("\n"):
                if posicion is not '':
                    nueva_posicion = {}
                    print(posicion)
                    try:
                        tipo, hora_gcm, validez, latitud, polo, longitud, hemisferio, dato1, dato2, fecha, dato3, dato4, dato5 = posicion.split(",")

                        if latitud is not '' and longitud is not '':
                            tiempo_hora = datetime( int(fecha[4:6]), int(fecha[2:4]), int(fecha[0:2]), int(hora_gcm[0:2]), int(hora_gcm[2:4]), int(hora_gcm[4:6]))

                            nueva_posicion["timestamp"] = datetime.timestamp(tiempo_hora)
                            nueva_posicion["latitud"] = (int(latitud[0:2]) + (float(latitud[2:9]) / 60)) * cuadrantes[polo]
                            nueva_posicion["longitud"] = (int(longitud[0:3]) + (float(longitud[3:10]) / 60)) * cuadrantes[hemisferio]
                            nueva_posicion["tiempo_de_parada"] = 0

                            if tipo == "$PARADA" and ultima_posicion is not None:
                                ultima_posicion["tiempo_de_parada"] = nueva_posicion["timestamp"] - ultima_posicion["timestamp"]

                            posiciones_parseadas.append(nueva_posicion)
                            ultima_posicion = nueva_posicion
                    except Exception:
                        pass

            if len(posiciones_parseadas) > 0:
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
            output.append({"posicion": {
                "timestamp": location["timestamp"],
                "latitud": location["latitud"],
                "longitud": location["longitud"],
                "tiempoDeParada": location["tiempo_de_parada"]
            }})
        return jsonify(output)

    return app