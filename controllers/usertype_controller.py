from flask import Blueprint, jsonify, request
from services.usertype_service.usertype_service import UserTypeService

route: str = '/usertype'
usertype_blueprint = Blueprint('usertype', __name__)
userTypeService = UserTypeService()


@usertype_blueprint.route(route, methods=['GET'])
def get_all_usertype():
    try:
        # Use the UserTypeService to fetch all user types
        user_types = userTypeService.get_all_usertype()

        # Convert user type objects to a list of dictionaries
        if user_types:
            user_type_data = [{"id": ut.id, "type": ut.type} for ut in user_types]

            # Return user type data as JSON
            return jsonify(user_type_data)
        else:
            return jsonify({'message': 'No user types found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving user types', 'details': str(e)}), 500


@usertype_blueprint.route(route + '/<int:usertype_id>', methods=['GET'])
def get_usertype(usertype_id: int):
    # Implement get usertype by id
    return jsonify({'message': 'Get usertype by id'})


@usertype_blueprint.route(route, methods=['POST'])
def create_usertype():
    try:
        # Extract the user type data from the request JSON
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Use the UserTypeService to create a new user type
        new_usertype = userTypeService.create_usertype(data)

        # Return a success response with the new user type data
        return jsonify({'message': 'User type created successfully',
                        'usertype': {'id': new_usertype.id, 'type': new_usertype.type}}), 201

    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the user type', 'details': str(e)}), 500


@usertype_blueprint.route(route + '/<int:usertype_id>', methods=['PUT'])
def update_usertype(usertype_id: int):
    try:
        # Extract the updated user type data from the request JSON
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Use the UserTypeService to update the user type
        updated_usertype = userTypeService.update_usertype(usertype_id, data)

        if updated_usertype:
            return jsonify({'message': 'User type updated successfully'})
        else:
            return jsonify({'error': 'User type not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating user type', 'details': str(e)}), 500


@usertype_blueprint.route(route + '/<int:usertype_id>', methods=['DELETE'])
def delete_usertype(usertype_id: int):
    try:
        deleted_usertype = userTypeService.delete_usertype(usertype_id)
        if deleted_usertype:
            return jsonify({'message': 'User type deleted successfully'})
        else:
            return jsonify({'error': 'User type not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting user type', 'details': str(e)}), 500
