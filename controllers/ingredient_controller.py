from datetime import datetime

from flask import Blueprint, jsonify, request

from services.ingredient_service.ingredient_service import IngredientService

route: str = '/ingredient'
ingredient_blueprint = Blueprint('ingredient', __name__, url_prefix=route)
ingredientService = IngredientService()


@ingredient_blueprint.route(route, methods=['GET'])
def get_all_ingredient():
    try:
        # Retrieve all ingredients using your service
        ingredients = ingredientService.get_all_ingredients()

        if ingredients:
            # Convert ingredients to a list of dictionaries or DTOs
            ingredient_data = [{
                "id": ingredient.id,
                "name": ingredient.name,
                "description": ingredient.description,
                "amount": ingredient.amount,
                "unit_id": ingredient.unit_id,
                "bb_date": ingredient.bb_date.strftime('%Y-%m-%d'),
                "last_restocked": ingredient.last_restocked.strftime('%Y-%m-%d'),
                "sort_ingredient_id": ingredient.sort_ingredient_id
            } for ingredient in ingredients]

            return jsonify(ingredient_data), 200

        return jsonify({'message': 'No ingredients found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving ingredients', 'details': str(e)}), 500


@ingredient_blueprint.route(route + '/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id: int):
    try:
        # Retrieve an ingredient by its ID using your service
        ingredient = ingredientService.get_ingredient_by_id(ingredient_id)

        if ingredient:
            # Convert the ingredient to a dictionary or DTO
            ingredient_data = {
                "id": ingredient.id,
                "name": ingredient.name,
                "description": ingredient.description,
                "amount": ingredient.amount,
                "unit_id": ingredient.unit_id,
                "bb_date": ingredient.bb_date.strftime('%Y-%m-%d'),
                "last_restocked": ingredient.last_restocked.strftime('%Y-%m-%d'),
                "sort_ingredient_id": ingredient.sort_ingredient_id
            }

            return jsonify(ingredient_data), 200

        return jsonify({'message': 'Ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the ingredient', 'details': str(e)}), 500


@ingredient_blueprint.route(route, methods=['POST'])
def create_ingredient():
    try:
        # Extract ingredient data from the request JSON
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Call the create_ingredient method from your service
        new_ingredient = ingredientService.create_ingredient(
            data.get('name'),
            data.get('sort_ingredient_id'),
            data.get('description'),
            data.get('amount'),
            data.get('unit_id'),
            datetime.strptime(data.get('bb_date'), '%Y-%m-%d').date(),
            datetime.strptime(data.get('last_restocked'), '%Y-%m-%d').date()
        )

        if new_ingredient:
            # Return a success response with the new ingredient data
            ingredient_data = {
                "id": new_ingredient.id,
                "name": new_ingredient.name,
                "description": new_ingredient.description,
                "amount": new_ingredient.amount,
                "unit_id": new_ingredient.unit_id,
                "bb_date": new_ingredient.bb_date.strftime('%Y-%m-%d'),
                "last_restocked": new_ingredient.last_restocked.strftime('%Y-%m-%d'),
                "sort_ingredient_id": new_ingredient.sort_ingredient_id
            }
            return jsonify({'message': 'Ingredient created successfully', 'ingredient': ingredient_data}), 201

        return jsonify({'error': 'An error occurred while creating the ingredient'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the ingredient', 'details': str(e)}), 500


@ingredient_blueprint.route(route + '/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id: int):
    try:
        # Extract ingredient data from the request JSON
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Call the update_ingredient method from your service
        updated = ingredientService.update_ingredient(
            ingredient_id,
            data.get('name'),
            data.get('sort_ingredient_id'),
            data.get('description'),
            data.get('amount'),
            data.get('unit_id'),
            datetime.strptime(data.get('bb_date'), '%Y-%m-%d').date(),
            datetime.strptime(data.get('last_restocked'), '%Y-%m-%d').date()
        )

        if updated:
            return jsonify({'message': 'Ingredient updated successfully'}), 200

        return jsonify({'error': 'An error occurred while updating the ingredient '
                                 'or the ingredient was not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the ingredient', 'details': str(e)}), 500


@ingredient_blueprint.route(route + '/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id: int):
    try:
        # Call the delete_ingredient method from your service
        deleted = ingredientService.delete_ingredient(ingredient_id)

        if deleted:
            return jsonify({'message': 'Ingredient deleted successfully'}), 200

        return jsonify({'error': 'An error occurred while deleting the ingredient '
                                 'or the ingredient was not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the ingredient', 'details': str(e)}), 500
