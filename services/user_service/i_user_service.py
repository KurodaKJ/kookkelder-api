from abc import ABC, abstractmethod


class IUserService(ABC):
    @abstractmethod
    def create_user(self, username, password):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def get_user_by_username(self, username):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def update_user(self, user_id, username, password):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass
