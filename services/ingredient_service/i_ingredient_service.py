from abc import ABC, abstractmethod


class IIngredientService(ABC):
    @abstractmethod
    def create_ingredient(self, ingredient_name, ingredient_type_id, description,
                          amount, unit_id, bb_date, last_restocked):
        pass

    @abstractmethod
    def get_ingredient_by_id(self, ingredient_id):
        pass

    @abstractmethod
    def get_ingredient_by_name(self, ingredient_name):
        pass

    @abstractmethod
    def get_all_ingredients(self):
        pass

    @abstractmethod
    def update_ingredient(self, ingredient_id, ingredient_name, ingredient_type_id,
                          description, amount, unit_id, bb_date, last_restocked):
        pass

    @abstractmethod
    def delete_ingredient(self, ingredient_id):
        pass

    @abstractmethod
    def get_expiring_ingredients(self, days_until_expiration):
        pass
