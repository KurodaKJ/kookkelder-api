from abc import ABC, abstractmethod


class IPictureService(ABC):
    @abstractmethod
    def __init__(self, upload_folder):
        pass

    @abstractmethod
    def upload_picture(self, file):
        pass

    @abstractmethod
    def get_picture(self, file):
        pass
