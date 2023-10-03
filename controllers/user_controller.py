from flask import jsonify, request
from app import app, db
from models.user_model import UserTypeModel

route: str = '/user'


@app.route(route + '/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route(route + '/test')
def test():
    return jsonify({'message': 'Test API'})


@app.route(route + '/usertype', methods=['GET'])
def get_usertype():
    try:
        # Query the database to retrieve all user types
        user_types = UserTypeModel.query.all()

        # Convert the user type objects to DTOs or dictionaries
        user_type_data = [{"id": ut.id, "type": ut.type} for ut in user_types]

        # Return the user type data as a list of dictionaries
        return jsonify(user_type_data)

    except Exception as e:
        # Handle any exceptions that may occur during the process
        return jsonify({'error': 'An error occurred while retrieving user types', 'details': str(e)}), 500


@app.route(route + '/usertype', methods=['POST'])
def create_usertype():
    try:
        # Extract the usertype data from the request JSON
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid data provided'}), 400

        # Create a new UserTypeModel object and add it to the database
        new_usertype = UserTypeModel(**data)
        db.session.add(new_usertype)
        db.session.commit()

        # Return a success response with the new usertype data
        return jsonify({'message': 'User type created successfully', 'usertype': data}), 201

    except Exception as e:
        # Handle any exceptions that may occur during the process
        return jsonify({'error': 'An error occurred while creating the user type', 'details': str(e)}), 500
