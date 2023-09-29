from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/kookkelder'

db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test')
def test():
    return jsonify({'message': 'Test API'})


if __name__ == '__main__':
    app.run()
