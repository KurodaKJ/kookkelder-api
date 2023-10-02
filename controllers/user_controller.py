from flask import jsonify
from app import app

route: str = '/user'


@app.route(route + '/hello')
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route(route + '/test')
def test():
    return jsonify({'message': 'Test API'})
