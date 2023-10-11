from flask import Blueprint, jsonify
from services.usertype_service.usertype_service import UserTypeService

route: str = '/usertype'
usertype_blueprint = Blueprint('usertype', __name__)
userTypeService = UserTypeService()


@usertype_blueprint.route(route, methods=['GET'])
def get_all_usertype():
    try:
        # Use the UserTypeService to fetch all user types
        user_types = userTypeService.get_usertype()

        # Convert user type objects to a list of dictionaries
        user_type_data = [{"id": ut.id, "type": ut.type} for ut in user_types]

        # Return user type data as JSON
        return jsonify(user_type_data)

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving user types', 'details': str(e)}), 500


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
