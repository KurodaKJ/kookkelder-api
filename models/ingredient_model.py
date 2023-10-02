from app import db


class IngredientModel(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1000))
    amount = db.Column(db.Float, nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    bb_date = db.Column(db.Date, nullable=False)
    last_restocked = db.Column(db.Date, nullable=False)
    sort_ingredient_id = db.Column(db.Integer, db.ForeignKey('sort_ingredients.id'), nullable=False)


class SortIngredientModel(db.Model):
    __tablename__ = 'sort_ingredients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)