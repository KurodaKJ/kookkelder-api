from flask import Blueprint, jsonify, request
from services.recipe_ingredient_service.recipe_ingredient_service import RecipeIngredientService
import sys
sys.path.append('../models/recipe_model.py/RecipeIngredientModel')

route: str = '/recipe-ingredient'
recipe_ingredient_blueprint = Blueprint('recipe_ingredient', __name__)
recipe_ingredient_service = RecipeIngredientService()


@recipe_ingredient_blueprint.route(route, methods=['GET'])
def get_all_recipe_ingredient():
    try:
        # Implement get all recipe ingredient
        recipe_ingredients = recipe_ingredient_service.get_all_recipe_ingredients()

        if recipe_ingredients:
            # Convert RecipeIngredientModel objects to dictionaries
            recipe_ingredient_dicts = [recipe.as_dict() for recipe in recipe_ingredients]
            return jsonify(recipe_ingredient_dicts)
        else:
            return jsonify({'message': 'No recipe ingredients found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve recipe ingredients', 'details': str(e)}), 500


@recipe_ingredient_blueprint.route(route + '/<int:recipe_ingredient_id>', methods=['GET'])
def get_recipe_ingredient(recipe_ingredient_id: int):
    try:
        # Implement get recipe ingredient by id
        recipe_ingredient = recipe_ingredient_service.get_recipe_ingredient_by_id(recipe_ingredient_id)

        if recipe_ingredient:
            return jsonify(recipe_ingredient)
        else:
            return jsonify({'message': 'Recipe ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve recipe ingredient', 'details': str(e)}), 500


@recipe_ingredient_blueprint.route(route, methods=['POST'])
def create_recipe_ingredient():
    try:
        # Implement create recipe ingredient
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        recipe_id = data.get('recipe_id')
        ingredient_id = data.get('ingredient_id')
        unit_id = data.get('unit_id')
        amount = data.get('amount')

        if None in [recipe_id, ingredient_id, unit_id, amount]:
            return jsonify({'error': 'Missing required fields in data'}), 400

        created_recipe_ingredient = recipe_ingredient_service.create_recipe_ingredient(recipe_id, ingredient_id,
                                                                                       unit_id, amount)
        return jsonify({'message': 'Recipe ingredient created successfully',
                        'recipe_ingredient': created_recipe_ingredient}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create recipe ingredient', 'details': str(e)}), 500


@recipe_ingredient_blueprint.route(route + '/<int:recipe_ingredient_id>', methods=['PUT'])
def update_recipe_ingredient(recipe_ingredient_id: int):
    try:
        # Implement update recipe ingredient
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        recipe_id = data.get('recipe_id')
        ingredient_id = data.get('ingredient_id')
        unit_id = data.get('unit_id')
        amount = data.get('amount')

        if None in [recipe_id, ingredient_id, unit_id, amount]:
            return jsonify({'error': 'Missing required fields in data'}), 400

        updated = recipe_ingredient_service.update_recipe_ingredient(recipe_ingredient_id, recipe_id,
                                                                     ingredient_id, unit_id, amount)
        if updated:
            return jsonify({'message': 'Recipe ingredient updated successfully'})
        else:
            return jsonify({'error': 'Recipe ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to update recipe ingredient', 'details': str(e)}), 500


@recipe_ingredient_blueprint.route(route + '/<int:recipe_ingredient_id>', methods=['DELETE'])
def delete_recipe_ingredient(recipe_ingredient_id: int):
    try:
        # Implement delete recipe ingredient
        deleted = recipe_ingredient_service.delete_recipe_ingredient(recipe_ingredient_id)
        if deleted:
            return jsonify({'message': 'Recipe ingredient deleted successfully'})
        else:
            return jsonify({'error': 'Recipe ingredient not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to delete recipe ingredient', 'details': str(e)}), 500
