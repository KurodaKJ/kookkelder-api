from app import db
from models.user_model import UserTypeModel
from services.usertype_service.i_usertype_service import IUserTypeService


class UserTypeService(IUserTypeService):
    def get_usertype(self):
        return UserTypeModel.query.all()

    def create_usertype(self, usertype):
        new_usertype = UserTypeModel(**usertype)
        db.session.add(new_usertype)
        db.session.commit()
        return new_usertype

    def update_usertype(self, usertype_id, usertype):
        pass

    def delete_usertype(self, usertype_id):
        pass
