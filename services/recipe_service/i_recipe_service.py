from abc import ABC, abstractmethod


class IRecipeService(ABC):
    @abstractmethod
    def create_recipe(self, recipe_name, recipe_description, recipe_type_id, recipe_image):
        pass

    @abstractmethod
    def get_recipe_by_id(self, recipe_id):
        pass

    @abstractmethod
    def get_recipe_by_name(self, recipe_name):
        pass

    @abstractmethod
    def get_all_recipes(self):
        pass

    @abstractmethod
    def update_recipe(self, recipe_id, recipe_name, recipe_description, recipe_type_id, recipe_image):
        pass

    @abstractmethod
    def delete_recipe(self, recipe_id):
        pass
