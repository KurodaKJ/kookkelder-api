from flask import Blueprint, request, jsonify
from services.picture_service.picture_service import PictureService

route: str = '/upload'
picture_blueprint = Blueprint('picture', __name__)

UPLOAD_FOLDER = '../upload'  # Adjust to your project's structure
picture_service = PictureService(UPLOAD_FOLDER)


@picture_blueprint.route(route, methods=['POST'])
def upload_picture():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            filename = picture_service.upload_picture(file)
            return jsonify({'message': 'Picture uploaded successfully', 'filename': filename}), 201

        return jsonify({'error': 'No file provided'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while uploading the picture', 'details': str(e)}), 500
