from services.recipe_service.i_recipe_service import IRecipeService


class RecipeService(IRecipeService):
    def __init__(self, recipe_repository):
        self.recipe_repository = recipe_repository

    def create_recipe(self, recipe_name, recipe_description, recipe_type_id, recipe_image):
        return self.recipe_repository.create_recipe(recipe_name, recipe_description, recipe_type_id, recipe_image)

    def get_recipe_by_id(self, recipe_id):
        return self.recipe_repository.get_recipe_by_id(recipe_id)

    def get_recipe_by_name(self, recipe_name):
        return self.recipe_repository.get_recipe_by_name(recipe_name)

    def get_all_recipes(self):
        return self.recipe_repository.get_all_recipes()

    def update_recipe(self, recipe_id, recipe_name, recipe_description, recipe_type_id, recipe_image):
        return self.recipe_repository.update_recipe(recipe_id, recipe_name, recipe_description, recipe_type_id, recipe_image)

    def delete_recipe(self, recipe_id):
        return self.recipe_repository.delete_recipe(recipe_id)

    def get_recipe_type_by_id(self, recipe_type_id):
        return self.recipe_repository.get_recipe_type_by_id(recipe_type_id)