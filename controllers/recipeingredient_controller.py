from flask import Blueprint, jsonify

route: str = '/recipe-ingredient'
recipeingredient_blueprint = Blueprint('recipeingredient', __name__)


@recipeingredient_blueprint.route(route, methods=['GET'])
def get_all_recipeingredient():
    # Implement get all recipeingredient
    return jsonify({'message': 'Get all recipeingredient'})


@recipeingredient_blueprint.route(route + '/<int:recipeingredient_id>', methods=['GET'])
def get_recipeingredient(recipeingredient_id: int):
    # Implement get recipeingredient by id
    return jsonify({'message': 'Get recipeingredient by id'})


@recipeingredient_blueprint.route(route, methods=['POST'])
def create_recipeingredient():
    # Implement create recipeingredient
    return jsonify({'message': 'Create recipeingredient'})


@recipeingredient_blueprint.route(route + '/<int:recipeingredient_id>', methods=['PUT'])
def update_recipeingredient(recipeingredient_id: int):
    # Implement update recipeingredient
    return jsonify({'message': 'Update recipeingredient'})


@recipeingredient_blueprint.route(route + '/<int:recipeingredient_id>', methods=['DELETE'])
def delete_recipeingredient(recipeingredient_id: int):
    # Implement delete recipeingredient
    return jsonify({'message': 'Delete recipeingredient'})