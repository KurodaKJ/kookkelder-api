import os
from services.picture_service.i_picture_service import IPictureService


class PictureService(IPictureService):
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder

    def upload_picture(self, file):
        try:
            if file:
                # Upload the picture to the server
                file.save(os.path.join(self.upload_folder, file.filename))

                # Return the picture's filename
                return file.filename
            else:
                raise Exception('No file provided')
        except Exception as e:
            # Handle any exceptions that may occur during picture upload
            raise e

    def get_picture(self, filename):
        try:
            # Check if the file exists
            file_path = os.path.join(self.upload_folder, filename)

            if os.path.exists(file_path):
                # You can return the file as binary data
                with open(file_path, 'rb') as file:
                    binary_data = file.read()
                return binary_data
            else:
                return None
        except Exception as e:
            raise e
