import random
from flask import Flask
import json
# importation de la bibliothèque
import requests
import pickle
import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import pandas as pd
import requests
import random as rd
from bson.json_util import dumps
import pickle


app = Flask(__name__)
CORS(app)
mongo_db = PyMongo(app, uri='mongodb://127.0.0.1:27017/minfopra')
db = mongo_db.db


@app.route('/Agent/load')
def solde():
    # id=requests.args.get('id')
    val = []
    result = db.detected.find()
    for i in result:
        val.append(i)
    return json.loads(dumps(val))


if __name__ == '__main__':
    app.run(debug=True, port=7000)
    print("lancement")
