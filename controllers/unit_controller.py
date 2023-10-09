from flask import Blueprint, jsonify

route: str = '/unit'
unit_blueprint = Blueprint('unit_blueprint', __name__)


@unit_blueprint.route(route, methods=['GET'])
def get_all_unit():
    # Implement get all unit
    return jsonify({'message': 'Get all unit'})


@unit_blueprint.route(route + '/<int:unit_id>', methods=['GET'])
def get_unit(unit_id: int):
    # Implement get unit by id
    return jsonify({'message': 'Get unit by id'})


@unit_blueprint.route(route, methods=['POST'])
def create_unit():
    # Implement create unit
    return jsonify({'message': 'Create unit'})


@unit_blueprint.route(route + '/<int:unit_id>', methods=['PUT'])
def update_unit(unit_id: int):
    # Implement update unit
    return jsonify({'message': 'Update unit'})


@unit_blueprint.route(route + '/<int:unit_id>', methods=['DELETE'])
def delete_unit(unit_id: int):
    # Implement delete unit
    return jsonify({'message': 'Delete unit'})