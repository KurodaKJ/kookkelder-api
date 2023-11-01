from flask import Blueprint, jsonify, request
from services.recipe_service.recipe_service import RecipeService

route: str = '/recipe'
recipe_service = RecipeService()
recipe_blueprint = Blueprint('recipe', __name__)


@recipe_blueprint.route(route, methods=['GET'])
def get_all_recipe():
    try:
        # Call the service to retrieve all recipes
        recipes = recipe_service.get_all_recipes()

        if recipes:
            # Convert the recipes to a list of dictionaries for JSON response
            recipe_data = [{"id": recipe.id, "name": recipe.name, "description": recipe.description, "preparation_time": recipe.preparation_time, "cooking_time": recipe.cooking_time} for recipe in recipes]
            return jsonify(recipe_data)
        else:
            return jsonify({'message': 'No recipes found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving recipes', 'details': str(e)}), 500


@recipe_blueprint.route(route + '/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id: int):
    try:
        # Call the service to retrieve a recipe by its ID
        recipe = recipe_service.get_recipe_by_id(recipe_id)
        if recipe:
            # Convert the recipe to a dictionary for JSON response
            recipe_data = {"id": recipe.id, "name": recipe.name, "description": recipe.description}
            return jsonify(recipe_data)
        else:
            return jsonify({'message': 'Recipe not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the recipe', 'details': str(e)}), 500


@recipe_blueprint.route(route + '/sorted-by-bb-date', methods=['GET'])
def get_all_recipes_by_bb_date():
    try:
        # Call the service to retrieve all recipes sorted by BB date
        recipes = recipe_service.get_all_recipes_by_bb_date()

        if recipes:
            # Convert the recipes to a list of dictionaries for JSON response
            recipe_data = [
                {
                    "id": recipe.id,
                    "name": recipe.name,
                    "description": recipe.description,
                    "preparation_time": recipe.preparation_time,
                    "cooking_time": recipe.cooking_time,
                }
                for recipe in recipes
            ]
            return jsonify(recipe_data)
        else:
            return jsonify({'message': 'No recipes found'}), 404
    except Exception as e:
        return jsonify(
            {'error': 'An error occurred while retrieving recipes', 'details': str(e)}
        ), 500


@recipe_blueprint.route(route, methods=['POST'])
def create_recipe():
    try:
        # Extract recipe data from the request JSON
        data = request.json
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Call the service to create a new recipe
        new_recipe = recipe_service.create_recipe(data['name'], data['description'],
                                                  data['preparation_time'], data['cooking_time'])
        # Convert the new recipe to a dictionary for JSON response
        recipe_data = {"id": new_recipe.id, "name": new_recipe.name, "description": new_recipe.description}
        return jsonify({'message': 'Recipe created successfully', 'recipe': recipe_data}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the recipe', 'details': str(e)}), 500


@recipe_blueprint.route(route + '/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id: int):
    try:
        # Extract recipe data from the request JSON
        data = request.json
        if not data or ('name' not in data and 'description' not in data):
            return jsonify({'error': 'Invalid data provided'}), 400

        # Call the service to update the recipe
        updated_recipe = recipe_service.update_recipe(
            recipe_id, data.get('name'), data.get('description'),
            data.get('preparation_time'), data.get('cooking_time'))
        if updated_recipe:
            # Convert the updated recipe to a dictionary for JSON response
            recipe_data = {"id": updated_recipe.id, "name": updated_recipe.name,
                           "description": updated_recipe.description}
            return jsonify({'message': 'Recipe updated successfully', 'recipe': recipe_data})
        else:
            return jsonify({'message': 'Recipe not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the recipe', 'details': str(e)}), 500


@recipe_blueprint.route(route + '/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id: int):
    try:
        # Call the service to delete the recipe
        deleted_recipe = recipe_service.delete_recipe(recipe_id)
        if deleted_recipe:
            # Convert the deleted recipe to a dictionary for JSON response
            recipe_data = {"id": deleted_recipe.id, "name": deleted_recipe.name,
                           "description": deleted_recipe.description}
            return jsonify({'message': 'Recipe deleted successfully', 'recipe': recipe_data})
        else:
            return jsonify({'message': 'Recipe not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the recipe', 'details': str(e)}), 500
