from db_instance import db
from models.user_model import UserTypeModel
from services.usertype_service.i_usertype_service import IUserTypeService


class UserTypeService(IUserTypeService):
    def get_all_usertype(self):
        try:
            return UserTypeModel.query.all()
        except Exception as e:
            raise e

    def get_user_type_by_id(self, user_type_id):
        try:
            return UserTypeModel.query.get(user_type_id)
        except Exception as e:
            raise e

    def create_usertype(self, usertype):
        try:
            new_usertype = UserTypeModel(**usertype)
            db.session.add(new_usertype)
            db.session.commit()
            return new_usertype
        except Exception as e:
            db.session.rollback()
            raise e

    def update_usertype(self, usertype_id, usertype_data):
        try:
            user_type = UserTypeModel.query.get(usertype_id)
            if user_type:
                # Update the user type with the new data
                user_type.type = usertype_data['type']
                db.session.commit()
                return user_type
            else:
                return None
        except Exception as e:
            raise e

    def delete_usertype(self, usertype_id):
        try:
            usertype = UserTypeModel.query.get(usertype_id)
            if usertype:
                db.session.delete(usertype)
                db.session.commit()
            return usertype
        except Exception as e:
            raise e
