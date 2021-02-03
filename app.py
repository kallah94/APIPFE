from flask import Flask, request, json, jsonify
from bson import json_util
from flask_pymongo  import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/APIBase"
mongo = PyMongo(app)


@app.route("/setcritere", methods=['POST'])
def setcritere():
    data = json.loads(request.data)
    mongo.db.criteres.insert_one(data)
    return 'ok', 200


@app.route("/getcritere", methods=['GET'])
def getcriteres():
    data = list(mongo.db.criteres.find())
    data = json.dumps(data, default=json_util.default)
    return json.loads(data)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8085)
