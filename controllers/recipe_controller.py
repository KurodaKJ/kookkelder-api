from flask import Blueprint, jsonify

route: str = '/recipe'
recipe_blueprint = Blueprint('recipe', __name__)


@recipe_blueprint.route(route, methods=['GET'])
def get_all_recipe():
    # Implement get all recipe
    return jsonify({'message': 'Get all recipe'})


@recipe_blueprint.route(route + '/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id: int):
    # Implement get recipe by id
    return jsonify({'message': 'Get recipe by id'})


@recipe_blueprint.route(route, methods=['POST'])
def create_recipe():
    # Implement create recipe
    return jsonify({'message': 'Create recipe'})


@recipe_blueprint.route(route + '/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id: int):
    # Implement update recipe
    return jsonify({'message': 'Update recipe'})


@recipe_blueprint.route(route + '/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id: int):
    # Implement delete recipe
    return jsonify({'message': 'Delete recipe'})
