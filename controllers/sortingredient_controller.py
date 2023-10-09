from flask import Blueprint, jsonify

route: str = '/sort-ingredient'
sortingredient_blueprint = Blueprint('sortingredient', __name__)


@sortingredient_blueprint.route(route, methods=['GET'])
def get_all_sortingredient():
    # Implement get all sortingredient
    return jsonify({'message': 'Get all sortingredient'})


@sortingredient_blueprint.route(route + '/<int:sortingredient_id>', methods=['GET'])
def get_sortingredient(sortingredient_id: int):
    # Implement get sortingredient by id
    return jsonify({'message': 'Get sortingredient by id'})


@sortingredient_blueprint.route(route, methods=['POST'])
def create_sortingredient():
    # Implement create sortingredient
    return jsonify({'message': 'Create sortingredient'})


@sortingredient_blueprint.route(route + '/<int:sortingredient_id>', methods=['PUT'])
def update_sortingredient(sortingredient_id: int):
    # Implement update sortingredient
    return jsonify({'message': 'Update sortingredient'})


@sortingredient_blueprint.route(route + '/<int:sortingredient_id>', methods=['DELETE'])
def delete_sortingredient(sortingredient_id: int):
    # Implement delete sortingredient
    return jsonify({'message': 'Delete sortingredient'})
