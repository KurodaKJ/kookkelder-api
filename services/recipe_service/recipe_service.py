from db_instance import db
from models.recipe_model import RecipeModel
from services.recipe_service.i_recipe_service import IRecipeService


class RecipeService(IRecipeService):
    def create_recipe(self, recipe_name, recipe_description, preparation_time, cooking_time):
        try:
            # Create a new recipe and add it to the database
            recipe = RecipeModel(
                name=recipe_name,
                description=recipe_description,
                preparation_time=preparation_time,
                cooking_time=cooking_time
            )
            db.session.add(recipe)
            db.session.commit()
            return recipe
        except Exception as e:
            db.session.rollback()
            raise e

    def get_recipe_by_id(self, recipe_id):
        try:
            return RecipeModel.query.get(recipe_id)
        except Exception as e:
            raise e

    def get_recipe_by_name(self, recipe_name):
        try:
            return RecipeModel.query.filter_by(name=recipe_name).first()
        except Exception as e:
            raise e

    def get_all_recipes(self):
        try:
            return RecipeModel.query.all()
        except Exception as e:
            raise e

    def update_recipe(self, recipe_id, recipe_name, recipe_description, preparation_time, cooking_time):
        try:
            recipe = RecipeModel.query.get(recipe_id)
            if recipe:
                # Update the recipe with the new data
                recipe.name = recipe_name
                recipe.description = recipe_description
                recipe.preparation_time = preparation_time
                recipe.cooking_time = cooking_time
                db.session.commit()
            return recipe
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_recipe(self, recipe_id):
        try:
            recipe = RecipeModel.query.get(recipe_id)
            if recipe:
                db.session.delete(recipe)
                db.session.commit()
            return recipe
        except Exception as e:
            db.session.rollback()
            raise e
