from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
import json
import pdb

app = Flask(__name__)
# 2
mongo = MongoClient('localhost', 27017)
# 3
app.db = mongo.local
# 4
# api = Api(app)


@app.route('/my-page')
def my_page():
    return "Hello, my name is Fabio Lanzoni"


@app.route('/pets')
def pets_route(arg):
    pets = {[
        {
            'name': 'Charlie',
            'color': 'Brown'
        },
        {
            'name': 'Bingo',
            'color': 'Blue'
        }
    ]}


@app.route('/courses', methods=['GET', 'POST'])
def courses_route():

    courses_col = app.db.courses
    result = courses_col.insert_one({"name": "MOB", 'number': 2, "students": [
        {"name": "Eliel", 'age': 23},
        {"name": "Fernando", 'age': 22},
        {"name": "Juanito", 'age': 20}
    ]})

    # pdb.set_trace()
    return (None, 201, None)

# def insert():


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
