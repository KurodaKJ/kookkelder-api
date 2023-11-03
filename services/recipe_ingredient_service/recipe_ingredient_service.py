from db_instance import db
from models.recipe_model import RecipeIngredientModel
from services.recipe_ingredient_service.i_recipe_ingredient_service import IRecipeIngredientService


class RecipeIngredientService(IRecipeIngredientService):
    def create_recipe_ingredient(self, recipe_id, ingredient_id, unit_id, amount):
        try:
            recipe_ingredient = RecipeIngredientModel(
                recipe_id=recipe_id,
                ingredient_id=ingredient_id,
                unit_id=unit_id,
                amount=amount
            )
            db.session.add(recipe_ingredient)
            db.session.commit()

            return recipe_ingredient

        except Exception as e:
            raise e  # Raise the exception

    def get_recipe_ingredient_by_id(self, recipe_ingredient_id):
        try:
            recipe_ingredient = RecipeIngredientModel.query.get(recipe_ingredient_id)
            return recipe_ingredient

        except Exception as e:
            raise e

    def get_recipe_ingredient_by_recipe_id(self, recipe_id):
        try:
            recipe_ingredients = RecipeIngredientModel.query.filter_by(recipe_id=recipe_id).all()
            return recipe_ingredients

        except Exception as e:
            raise e

    def get_recipe_ingredient_by_ingredient_id(self, ingredient_id):
        try:
            recipe_ingredients = RecipeIngredientModel.query.filter_by(ingredient_id=ingredient_id).all()
            return recipe_ingredients

        except Exception as e:
            raise e

    def get_all_recipe_ingredients(self):
        try:
            recipe_ingredients = RecipeIngredientModel.query.all()
            return recipe_ingredients

        except Exception as e:
            raise e

    def update_recipe_ingredient(self, recipe_ingredient_id, recipe_id, ingredient_id, unit_id, amount):
        try:
            recipe_ingredient = RecipeIngredientModel.query.get(recipe_ingredient_id)

            if not recipe_ingredient:
                return False

            recipe_ingredient.recipe_id = recipe_id
            recipe_ingredient.ingredient_id = ingredient_id
            recipe_ingredient.unit_id = unit_id
            recipe_ingredient.amount = amount

            db.session.commit()
            return True

        except Exception as e:
            raise e

    def delete_recipe_ingredient(self, recipe_ingredient_id):
        try:
            recipe_ingredient = RecipeIngredientModel.query.get(recipe_ingredient_id)

            if not recipe_ingredient:
                return False

            db.session.delete(recipe_ingredient)
            db.session.commit()
            return True

        except Exception as e:
            raise e
