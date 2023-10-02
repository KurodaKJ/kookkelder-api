from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/kookkelder'

db = SQLAlchemy(app)
migration = Migrate(app, db)

from models.ingredient_model import IngredientModel, SortIngredientModel
from models.recipe_model import RecipeModel, RecipeIngredientModel, UnitModel
from models.user_model import UserModel, UserTypeModel


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test')
def test():
    return jsonify({'message': 'Test API'})


if __name__ == '__main__':
    app.run()
