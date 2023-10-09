from flask import Blueprint, jsonify

route: str = '/usertype'
usertype_blueprint = Blueprint('usertype', __name__)


@usertype_blueprint.route(route, methods=['GET'])
def get_all_usertype():
    # Implement get all usertype
    return jsonify({'message': 'Get all usertype'})


@usertype_blueprint.route(route + '/<int:usertype_id>', methods=['GET'])
def get_usertype(usertype_id: int):
    # Implement get usertype by id
    return jsonify({'message': 'Get usertype by id'})


@usertype_blueprint.route(route, methods=['POST'])
def create_usertype():
    # Implement create usertype
    return jsonify({'message': 'Create usertype'})


@usertype_blueprint.route(route + '/<int:usertype_id>', methods=['PUT'])
def update_usertype(usertype_id: int):
    # Implement update usertype
    return jsonify({'message': 'Update usertype'})


@usertype_blueprint.route(route + '/<int:usertype_id>', methods=['DELETE'])
def delete_usertype(usertype_id: int):
    # Implement delete usertype
    return jsonify({'message': 'Delete usertype'})
