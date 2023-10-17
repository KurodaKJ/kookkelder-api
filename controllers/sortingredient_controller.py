from flask import Blueprint, jsonify, request

from services.sortingredient_service.sortingredient_service import SortIngredientService

route: str = '/sort-ingredient'
sort_ingredient_blueprint = Blueprint('sort_ingredient', __name__)

# Create an instance of SortIngredientService
sort_ingredient_service = SortIngredientService()


@sort_ingredient_blueprint.route(route, methods=['GET'])
def get_all_sort_ingredient():
    try:
        # Implement get all sort ingredients
        sort_ingredients = sort_ingredient_service.get_all_sort_ingredients()

        if sort_ingredients:
            # Convert sort ingredients to dictionaries
            sort_ingredient_data = [{"id": si.id, "name": si.name} for si in sort_ingredients]
            return jsonify(sort_ingredient_data), 200
        else:
            return jsonify({'message': 'No sort ingredients found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving sort ingredients', 'details': str(e)}), 500


@sort_ingredient_blueprint.route(route + '/<int:sort_ingredient_id>', methods=['GET'])
def get_sort_ingredient(sort_ingredient_id: int):
    try:
        # Implement get sort ingredient by id
        sort_ingredient = sort_ingredient_service.get_sort_ingredient_by_id(sort_ingredient_id)
        if sort_ingredient:
            return jsonify({'id': sort_ingredient.id, 'name': sort_ingredient.name}), 200
        else:
            return jsonify({'message': 'Sort ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving sort ingredient', 'details': str(e)}), 500


@sort_ingredient_blueprint.route(route, methods=['POST'])
def create_sort_ingredient():
    try:
        # Extract data from the request JSON
        data = request.json
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Create a new sort ingredient
        sort_ingredient = sort_ingredient_service.create_sort_ingredient(data['name'])
        return jsonify({'message': 'Sort ingredient created successfully',
                        'sort ingredient': {'id': sort_ingredient.id, 'name': sort_ingredient.name}}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating sort ingredient', 'details': str(e)}), 500


@sort_ingredient_blueprint.route(route + '/<int:sort_ingredient_id>', methods=['PUT'])
def update_sort_ingredient(sort_ingredient_id: int):
    try:
        # Extract data from the request JSON
        data = request.json
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Update the sort ingredient
        sort_ingredient = sort_ingredient_service.update_sort_ingredient(sort_ingredient_id, data['name'])
        if sort_ingredient:
            return jsonify({'message': 'Sort ingredient updated successfully',
                            'sort ingredient': {'id': sort_ingredient.id, 'name': sort_ingredient.name}}), 200
        else:
            return jsonify({'message': 'Sort ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating sort ingredient', 'details': str(e)}), 500


@sort_ingredient_blueprint.route(route + '/<int:sort_ingredient_id>', methods=['DELETE'])
def delete_sort_ingredient(sort_ingredient_id: int):
    try:
        # Delete the sort ingredient
        success = sort_ingredient_service.delete_sort_ingredient(sort_ingredient_id)
        if success:
            return jsonify({'message': 'Sort ingredient deleted successfully'}), 200
        else:
            return jsonify({'message': 'Sort ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting sort ingredient', 'details': str(e)}), 500
