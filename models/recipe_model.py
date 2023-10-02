from app import db


class RecipeModel(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1000))
    preparation_time = db.Column(db.Float, nullable=False)
    cooking_time = db.Column(db.Float, nullable=False)


class RecipeIngredientModel(db.Model):
    __tablename__ = 'recipe_ingredients'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True, nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    unit = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)


class UnitModel(db.Model):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
