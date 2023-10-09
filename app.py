from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from flask_migrate import Migrate
from db_instance import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/kookkelder'

migration = Migrate(app, db)

# Import models for migration and database creation
from models.ingredient_model import IngredientModel, SortIngredientModel
from models.recipe_model import RecipeModel, RecipeIngredientModel, UnitModel
from models.user_model import UserModel, UserTypeModel

# Import controllers for API
from controllers import ingredient_controller, recipe_controller
from controllers.user_controller import user_blueprint

# Register blueprints for API
app.register_blueprint(user_blueprint)


@app.route('/')
def welcome():
    return jsonify({'message': 'Welcome to the Kookkelder API!'})


if __name__ == '__main__':
    app.run()
