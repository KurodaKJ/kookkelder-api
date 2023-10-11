
from db_instance import db
from models.user_model import UserTypeModel
from services.usertype_service.i_usertype_service import IUserTypeService


class UserTypeService(IUserTypeService):
    def get_all_usertype(self):
        return UserTypeModel.query.all()

    def get_user_type_by_id(self, user_type_id):
        pass

    def create_usertype(self, usertype):
        new_usertype = UserTypeModel(**usertype)
        db.session.add(new_usertype)
        db.session.commit()
        return new_usertype

    def update_usertype(self, usertype_id, usertype):
        pass

    def delete_usertype(self, usertype_id):
        try:
            usertype = UserTypeModel.query.get(usertype_id)
            if usertype:
                db.session.delete(usertype)
                db.session.commit()
            return usertype
        except Exception as e:
            raise e
