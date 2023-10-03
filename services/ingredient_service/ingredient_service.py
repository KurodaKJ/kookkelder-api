from services.ingredient_service.i_ingredient_service import IIngredientService


class IngredientService(IIngredientService):
    def __init__(self, ingredient_repository):
        self.ingredient_repository = ingredient_repository

    def create_ingredient(self, ingredient_name, ingredient_type_id):
        return self.ingredient_repository.create_ingredient(ingredient_name, ingredient_type_id)

    def get_ingredient_by_id(self, ingredient_id):
        return self.ingredient_repository.get_ingredient_by_id(ingredient_id)

    def get_ingredient_by_name(self, ingredient_name):
        return self.ingredient_repository.get_ingredient_by_name(ingredient_name)

    def get_all_ingredients(self):
        return self.ingredient_repository.get_all_ingredients()

    def update_ingredient(self, ingredient_id, ingredient_name, ingredient_type_id):
        return self.ingredient_repository.update_ingredient(ingredient_id, ingredient_name, ingredient_type_id)

    def delete_ingredient(self, ingredient_id):
        return self.ingredient_repository.delete_ingredient(ingredient_id)

    def get_ingredient_type_by_id(self, ingredient_type_id):
        return self.ingredient_repository.get_ingredient_type_by_id(ingredient_type_id)