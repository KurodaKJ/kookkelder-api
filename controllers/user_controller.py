from flask import Blueprint, jsonify, request
from services.user_service.user_service import UserService

route: str = '/user'
user_blueprint = Blueprint('user', __name__)

# Initialize the user service
user_service = UserService()


@user_blueprint.route(route + '/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@user_blueprint.route(route, methods=['GET'])
def get_all_users():
    try:
        users = user_service.get_all_users()
        if users:
            user_list = [{'id': user.id, 'username': user.username} for user in users]
            return jsonify({'users': user_list})
        else:
            return jsonify({'message': 'No users found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_blueprint.route(route + '/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    try:
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify({'user': {'id': user.id, 'username': user.username}})
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_blueprint.route(route, methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        usertype = data.get('usertype')

        if not username or not password or not usertype:
            return jsonify({'error': 'Both username and password are required'}), 400

        new_user = user_service.create_user(username, password, usertype)
        if new_user:
            return jsonify({'message': 'User created successfully', 'user': {'id': new_user.id,
                                                                             'username': new_user.username,
                                                                             'usertype': new_user.usertype}})
        else:
            return jsonify({'error': 'Failed to create user'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_blueprint.route(route + '/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        usertype = data.get('usertype')

        if not username or not password:
            return jsonify({'error': 'Both username and password are required'}), 400

        user = user_service.update_user(user_id, username, password, usertype)
        if user:
            return jsonify({'message': 'User updated successfully', 'user': {'id': user.id,
                                                                             'username': user.username,
                                                                             'usertype': user.usertype}})
        else:
            return jsonify({'error': 'User not found or failed to update user'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_blueprint.route(route + '/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    try:
        user = user_service.delete_user(user_id)
        if user:
            return jsonify({'message': 'User deleted successfully', 'user': {'id': user.id,
                                                                             'username': user.username,
                                                                             'usertype': user.usertype}})
        else:
            return jsonify({'error': 'User not found or failed to delete user'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
