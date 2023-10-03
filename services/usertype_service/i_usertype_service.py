from abc import ABC, abstractmethod


class IUserTypeService(ABC):
    @abstractmethod
    def get_usertype(self):
        pass

    @abstractmethod
    def create_usertype(self, usertype):
        pass

    @abstractmethod
    def update_usertype(self, usertype_id, usertype):
        pass

    @abstractmethod
    def delete_usertype(self, usertype_id):
        pass
