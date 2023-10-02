from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/kookkelder'

db = SQLAlchemy(app)
migration = Migrate(app, db)

# Import models for migration and database creation
from models.ingredient_model import IngredientModel, SortIngredientModel
from models.recipe_model import RecipeModel, RecipeIngredientModel, UnitModel
from models.user_model import UserModel, UserTypeModel

# Import controllers for API
from controllers import user_controller, ingredient_controller, recipe_controller


@app.route('/')
def welcome():
    return jsonify({'message': 'Welcome to the Kookkelder API!'})


if __name__ == '__main__':
    app.run()
