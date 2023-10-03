from services.user_service.i_user_service import IUserService


class UserService(IUserService):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, username, password):
        return self.user_repository.create_user(username, password)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_username(self, username):
        return self.user_repository.get_user_by_username(username)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, username, password):
        return self.user_repository.update_user(user_id, username, password)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

    def get_user_type_by_id(self, user_type_id):
        return self.user_repository.get_user_type_by_id(user_type_id)