from models.user_model import UserModel
from services.user_service.i_user_service import IUserService


class UserService(IUserService):
    def create_user(self, username, password):
        pass

    def get_user_by_id(self, user_id):
        pass

    def get_user_by_username(self, username):
        pass

    def get_all_users(self):
        return UserModel.query.all()

    def update_user(self, user_id, username, password):
        pass

    def delete_user(self, user_id):
        pass

    def get_user_type_by_id(self, user_type_id):
        pass
