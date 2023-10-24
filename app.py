from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from db_instance import db

# Import controllers for API
from controllers.user_controller import user_blueprint
from controllers.usertype_controller import usertype_blueprint
from controllers.ingredient_controller import ingredient_blueprint
from controllers.sortingredient_controller import sort_ingredient_blueprint
from controllers.recipe_controller import recipe_blueprint
from controllers.recipe_ingredient_controller import recipe_ingredient_blueprint
from controllers.unit_controller import unit_blueprint

app = Flask(__name__)
CORS(app)

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/kookkelder'
db.init_app(app)

# Configuration for migration
migration = Migrate(app, db)

# Import models for migration and database creation
from models.ingredient_model import IngredientModel, SortIngredientModel
from models.recipe_model import RecipeModel, RecipeIngredientModel, UnitModel
from models.user_model import UserModel, UserTypeModel


# Register blueprints for API
app.register_blueprint(user_blueprint)
app.register_blueprint(usertype_blueprint)
app.register_blueprint(ingredient_blueprint)
app.register_blueprint(sort_ingredient_blueprint)
app.register_blueprint(recipe_blueprint)
app.register_blueprint(recipe_ingredient_blueprint)
app.register_blueprint(unit_blueprint)


@app.route('/')
def welcome():
    return jsonify({'message': 'Welcome to the Kookkelder API!'})


if __name__ == '__main__':
    app.run()
