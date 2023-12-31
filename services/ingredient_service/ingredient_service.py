from datetime import datetime, timedelta
from db_instance import db
from models.ingredient_model import IngredientModel
from services.ingredient_service.i_ingredient_service import IIngredientService


class IngredientService(IIngredientService):

    def create_ingredient(self, ingredient_name, ingredient_type_id, description,
                          amount, unit_id, bb_date, last_restocked):
        try:
            # Create a new ingredient and add it to the database
            ingredient = IngredientModel(
                name=ingredient_name,
                sort_ingredient_id=ingredient_type_id,
                description=description,
                amount=amount,
                unit_id=unit_id,
                bb_date=bb_date,
                last_restocked=last_restocked
            )
            db.session.add(ingredient)
            db.session.commit()

            return ingredient  # Return the created ingredient object

        except Exception as e:
            # Handle any exceptions that may occur during ingredient creation
            raise e

    def get_ingredient_by_id(self, ingredient_id):
        try:
            # Query the database to retrieve an ingredient by its ID
            ingredient = IngredientModel.query.get(ingredient_id)
            return ingredient  # Return the ingredient object if found, or None if not found

        except Exception as e:
            # Handle any exceptions that may occur during ingredient retrieval
            raise e

    def get_ingredient_by_name(self, ingredient_name):
        try:
            # Query the database to retrieve an ingredient by its name
            ingredient = IngredientModel.query.filter_by(name=ingredient_name).first()
            return ingredient  # Return the ingredient object if found, or None if not found

        except Exception as e:
            # Handle any exceptions that may occur during ingredient retrieval
            raise e

    def get_all_ingredients(self):
        try:
            # Query the database to retrieve all ingredients
            ingredients = IngredientModel.query.all()
            return ingredients  # Return a list of ingredient objects

        except Exception as e:
            # Handle any exceptions that may occur during ingredient retrieval
            raise e

    def update_ingredient(self, ingredient_id, ingredient_name, ingredient_type_id,
                          description, amount, unit_id, bb_date, last_restocked):
        try:
            # Query the database to retrieve an ingredient by its ID
            ingredient = IngredientModel.query.get(ingredient_id)

            if not ingredient:
                return False  # Ingredient not found

            # Update the ingredient attributes
            ingredient.name = ingredient_name
            ingredient.sort_ingredient_id = ingredient_type_id
            ingredient.description = description
            ingredient.amount = amount
            ingredient.unit_id = unit_id
            ingredient.bb_date = bb_date
            ingredient.last_restocked = last_restocked

            db.session.commit()
            return True  # Ingredient updated successfully

        except Exception as e:
            # Handle any exceptions that may occur during ingredient update
            raise e

    def delete_ingredient(self, ingredient_id):
        try:
            # Query the database to retrieve an ingredient by its ID
            ingredient = IngredientModel.query.get(ingredient_id)

            if not ingredient:
                return False  # Ingredient not found

            db.session.delete(ingredient)
            db.session.commit()
            return True  # Ingredient deleted successfully

        except Exception as e:
            # Handle any exceptions that may occur during ingredient deletion
            raise e

    def get_expiring_ingredients(self, days_until_expiration):
        try:
            today = datetime.today()
            expiration_date = today + timedelta(days=days_until_expiration)
            expiring_ingredients = IngredientModel.query.filter(IngredientModel.bb_date <= expiration_date).all()
            return expiring_ingredients
        except Exception as e:
            raise e

    def get_top_ingredients(self, limit):
        try:
            # Query the database to retrieve the top ingredients with the biggest amounts
            top_ingredients = IngredientModel.query.order_by(IngredientModel.amount.desc()).limit(limit).all()
            return top_ingredients

        except Exception as e:
            # Handle any exceptions that may occur during ingredient retrieval
            raise e