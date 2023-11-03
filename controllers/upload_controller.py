import io
import os

from flask import Blueprint, request, jsonify, send_file
from services.picture_service.picture_service import PictureService

route: str = '/upload'
upload_blueprint = Blueprint('upload', __name__)

# Provide the absolute path to the target directory
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
picture_service = PictureService(UPLOAD_FOLDER)


@upload_blueprint.route(route, methods=['POST'])
def upload_picture():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            filename = picture_service.upload_picture(file, UPLOAD_FOLDER)
            return jsonify({'message': 'Picture uploaded successfully', 'filename': filename}), 201

        return jsonify({'error': 'No file provided'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while uploading the picture', 'details': str(e)}), 500


@upload_blueprint.route(route, methods=['GET'])
def get_picture():
    try:
        filename = request.args.get('filename')
        if filename:
            binary_data = picture_service.get_picture(filename)
            if binary_data:
                return send_file(
                    io.BytesIO(binary_data),
                    attachment_filename=filename,
                    as_attachment=True,
                    mimetype='application/octet-stream'
                )
            else:
                return jsonify({'error': 'File not found'}), 404
        else:
            return jsonify({'error': 'No filename provided'}), 400
    except Exception as e:
        return (jsonify({'error': 'An error occurred while retrieving the picture',
                         'details': str(e)}), 500)
