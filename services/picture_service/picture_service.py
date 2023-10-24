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
