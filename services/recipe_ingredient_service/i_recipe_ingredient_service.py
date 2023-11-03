from abc import ABC, abstractmethod


class IRecipeIngredientService(ABC):
    @abstractmethod
    def create_recipe_ingredient(self, recipe_id, ingredient_id, unit_id, amount):
        pass

    @abstractmethod
    def get_recipe_ingredient_by_id(self, recipe_ingredient_id):
        pass

    @abstractmethod
    def get_recipe_ingredient_by_recipe_id(self, recipe_id):
        pass

    @abstractmethod
    def get_recipe_ingredient_by_ingredient_id(self, ingredient_id):
        pass

    @abstractmethod
    def get_all_recipe_ingredients(self):
        pass

    @abstractmethod
    def update_recipe_ingredient(self, recipe_ingredient_id, recipe_id, ingredient_id, unit_id, amount):
        pass

    @abstractmethod
    def delete_recipe_ingredient(self, recipe_ingredient_id):
        pass
