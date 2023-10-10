from flask import Blueprint, jsonify, request

from services.sortingredient_service.sortingredient_service import SortIngredientService

route: str = '/sort-ingredient'
sortingredient_blueprint = Blueprint('sortingredient', __name__)

# Create an instance of SortIngredientService
sortingredient_service = SortIngredientService()


@sortingredient_blueprint.route(route, methods=['GET'])
def get_all_sortingredient():
    try:
        # Implement get all sortingredients
        sortingredients = sortingredient_service.get_all_sort_ingredients()
        # Convert sortingredients to dictionaries
        sortingredient_data = [{"id": si.id, "name": si.name} for si in sortingredients]
        return jsonify(sortingredient_data), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving sortingredients', 'details': str(e)}), 500


@sortingredient_blueprint.route(route + '/<int:sortingredient_id>', methods=['GET'])
def get_sortingredient(sortingredient_id: int):
    try:
        # Implement get sortingredient by id
        sortingredient = sortingredient_service.get_sort_ingredient_by_id(sortingredient_id)
        if sortingredient:
            return jsonify({'id': sortingredient.id, 'name': sortingredient.name}), 200
        else:
            return jsonify({'message': 'Sortingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving sortingredient', 'details': str(e)}), 500


@sortingredient_blueprint.route(route, methods=['POST'])
def create_sortingredient():
    try:
        # Extract data from the request JSON
        data = request.json
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Create a new sortingredient
        sortingredient = sortingredient_service.create_sort_ingredient(data['name'])
        return jsonify({'message': 'Sortingredient created successfully',
                        'sortingredient': {'id': sortingredient.id, 'name': sortingredient.name}}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating sortingredient', 'details': str(e)}), 500


@sortingredient_blueprint.route(route + '/<int:sortingredient_id>', methods=['PUT'])
def update_sortingredient(sortingredient_id: int):
    try:
        # Extract data from the request JSON
        data = request.json
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Update the sortingredient
        sortingredient = sortingredient_service.update_sort_ingredient(sortingredient_id, data['name'])
        if sortingredient:
            return jsonify({'message': 'Sortingredient updated successfully',
                            'sortingredient': {'id': sortingredient.id, 'name': sortingredient.name}}), 200
        else:
            return jsonify({'message': 'Sortingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating sortingredient', 'details': str(e)}), 500


@sortingredient_blueprint.route(route + '/<int:sortingredient_id>', methods=['DELETE'])
def delete_sortingredient(sortingredient_id: int):
    try:
        # Delete the sortingredient
        success = sortingredient_service.delete_sort_ingredient(sortingredient_id)
        if success:
            return jsonify({'message': 'Sortingredient deleted successfully'}), 200
        else:
            return jsonify({'message': 'Sortingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting sortingredient', 'details': str(e)}), 500
