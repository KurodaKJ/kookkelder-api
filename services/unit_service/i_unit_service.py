from abc import ABC, abstractmethod


class IUnitService(ABC):
    @abstractmethod
    def create_unit(self, unit_name):
        pass

    @abstractmethod
    def get_unit_by_id(self, unit_id):
        pass

    @abstractmethod
    def get_unit_by_name(self, unit_name):
        pass

    @abstractmethod
    def get_all_units(self):
        pass

    @abstractmethod
    def update_unit(self, unit_id, unit_name):
        pass

    @abstractmethod
    def delete_unit(self, unit_id):
        pass
