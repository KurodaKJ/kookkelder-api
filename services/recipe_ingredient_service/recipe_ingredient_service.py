from services.recipe_ingredient_service.i_recipe_ingredient_service import IRecipeIngredientService


class RecipeIngredientService(IRecipeIngredientService):
    def create_recipe_ingredient(self, recipe_id, ingredient_id, unit_id, amount):
        pass

    def get_recipe_ingredient_by_id(self, recipe_ingredient_id):
        pass

    def get_recipe_ingredient_by_recipe_id(self, recipe_id):
        pass

    def get_recipe_ingredient_by_ingredient_id(self, ingredient_id):
        pass

    def get_all_recipe_ingredients(self):
        pass

    def update_recipe_ingredient(self, recipe_ingredient_id, recipe_id, ingredient_id, unit_id, amount):
        pass

    def delete_recipe_ingredient(self, recipe_ingredient_id):
        pass
