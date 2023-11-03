from abc import ABC, abstractmethod


class ISortIngredientService(ABC):
    @abstractmethod
    def create_sort_ingredient(self, name: str):
        pass

    @abstractmethod
    def get_sort_ingredient_by_id(self, sort_ingredient_id: int):
        pass

    @abstractmethod
    def get_sort_ingredient_by_name(self, name: str):
        pass

    @abstractmethod
    def get_all_sort_ingredients(self) -> list:
        pass

    @abstractmethod
    def update_sort_ingredient(self, sort_ingredient_id: int, name: str):
        pass

    @abstractmethod
    def delete_sort_ingredient(self, sort_ingredient_id: int):
        pass
