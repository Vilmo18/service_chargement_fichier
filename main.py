from flask import Flask
# importation de la bibliothèque
import os

from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from script import process_csv

import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import pandas as pd
from bson.json_util import dumps
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app)
mongo_db = PyMongo(app, uri='mongodb://127.0.0.1:27017/minfopra')
db = mongo_db.db

ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


UPLOAD_FOLDER = 'upload'
app.config['DEBUG'] = True
app.config['FOLDER'] = UPLOAD_FOLDER


@app.route('/Agent/load', methods=['POST'])
def chargement():
    file = request.files['file']
    """if file and allowed_file(file.filename):
        print(allowed_file(file.filename))
        filename = secure_filename(file.filename)
        new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
        save_location = os.path.join('input', new_filename)
        file.save(save_location)"""
    print("le nom")
    print(file.filename)
    if file.filename != '':
        file_path = os.path.join(app.config['FOLDER'], file.filename)
        file.save(file_path)
    return 'ok'

    # output_file = process_csv(save_location)
    # return send_from_directory('output', output_file)
    # return redirect(url_for('download'))


if __name__ == '__main__':
    app.run(debug=True, port=7000)
    print("lancement")
