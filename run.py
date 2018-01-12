

from flask import Flask, render_template, redirect, url_for, request, jsonify, request
import json
from flask_cors import CORS


from flask_pymongo import PyMongo



app = Flask(__name__)
with app.app_context():
    CORS(app)
    app.config['MONGO_DBNAME'] = 'restdb'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
    mongo = PyMongo(app)

    from python_play import *

    if __name__ == '__main__':
        app.run(debug=True)
