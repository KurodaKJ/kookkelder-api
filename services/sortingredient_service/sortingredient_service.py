from db_instance import db
from models.ingredient_model import SortIngredientModel
from services.sortingredient_service.i_sortingredient_service import ISortIngredientService


class SortIngredientService(ISortIngredientService):
    def create_sort_ingredient(self, name):
        try:
            sort_ingredient = SortIngredientModel(name=name)
            db.session.add(sort_ingredient)
            db.session.commit()
            return sort_ingredient
        except Exception as e:
            db.session.rollback()
            raise e

    def get_sort_ingredient_by_id(self, sort_ingredient_id):
        return SortIngredientModel.query.get(sort_ingredient_id)

    def get_sort_ingredient_by_name(self, name):
        return SortIngredientModel.query.filter_by(name=name).first()

    def get_all_sort_ingredients(self):
        return SortIngredientModel.query.all()

    def update_sort_ingredient(self, sort_ingredient_id, name):
        try:
            sort_ingredient = SortIngredientModel.query.get(sort_ingredient_id)
            if sort_ingredient:
                sort_ingredient.name = name
                db.session.commit()
            return sort_ingredient
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_sort_ingredient(self, sort_ingredient_id):
        try:
            sort_ingredient = SortIngredientModel.query.get(sort_ingredient_id)
            if sort_ingredient:
                db.session.delete(sort_ingredient)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
