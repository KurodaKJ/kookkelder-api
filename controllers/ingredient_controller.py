from flask import Blueprint, jsonify

route: str = '/ingredient'
ingredient_blueprint = Blueprint('ingredient', __name__, url_prefix=route)


@ingredient_blueprint.route(route, methods=['GET'])
def get_all_ingredient():
    # Implement get all ingredient
    return jsonify({'message': 'Get all ingredient'})


@ingredient_blueprint.route(route + '/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id: int):
    # Implement get ingredient by id
    return jsonify({'message': 'Get ingredient by id'})


@ingredient_blueprint.route(route, methods=['POST'])
def create_ingredient():
    # Implement create ingredient
    return jsonify({'message': 'Create ingredient'})


@ingredient_blueprint.route(route + '/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id: int):
    # Implement update ingredient
    return jsonify({'message': 'Update ingredient'})


@ingredient_blueprint.route(route + '/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id: int):
    # Implement delete ingredient
    return jsonify({'message': 'Delete ingredient'})