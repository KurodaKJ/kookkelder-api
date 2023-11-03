from db_instance import db
from models.recipe_model import UnitModel
from services.unit_service.i_unit_service import IUnitService


class UnitService(IUnitService):
    def create_unit(self, unit_name):
        try:
            unit = UnitModel(name=unit_name)
            db.session.add(unit)
            db.session.commit()
            return unit
        except Exception as e:
            db.session.rollback()
            raise e

    def get_unit_by_id(self, unit_id):
        try:
            unit = UnitModel.query.get(unit_id)
            return unit
        except Exception as e:
            raise e

    def get_unit_by_name(self, unit_name):
        try:
            unit = UnitModel.query.filter_by(name=unit_name).first()
            return unit
        except Exception as e:
            raise e

    def get_all_units(self):
        try:
            units = UnitModel.query.all()
            return units
        except Exception as e:
            raise e

    def update_unit(self, unit_id, unit_name):
        try:
            unit = UnitModel.query.get(unit_id)
            if unit:
                unit.name = unit_name
                db.session.commit()
            return unit
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_unit(self, unit_id):
        try:
            unit = UnitModel.query.get(unit_id)
            if unit:
                db.session.delete(unit)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
