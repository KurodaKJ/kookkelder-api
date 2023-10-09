from flask import Blueprint, jsonify

route: str = '/user'
user_blueprint = Blueprint('user', __name__)


@user_blueprint.route(route + '/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@user_blueprint.route(route, methods=['GET'])
def get_all_user():
    # Implement get all user
    return jsonify({'message': 'Get all user'})


@user_blueprint.route(route + '/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    # Implement get user by id
    return jsonify({'message': 'Get user by id'})


@user_blueprint.route(route, methods=['POST'])
def create_user():
    # Implement create user
    return jsonify({'message': 'Create user'})


@user_blueprint.route(route + '/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    # Implement update user
    return jsonify({'message': 'Update user'})


@user_blueprint.route(route + '/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    # Implement delete user
    return jsonify({'message': 'Delete user'})
