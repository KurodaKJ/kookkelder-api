from flask import Blueprint, jsonify, request
from services.unit_service.unit_service import UnitService

unit_service = UnitService()
route: str = '/unit'
unit_blueprint = Blueprint('unit_blueprint', __name__)


@unit_blueprint.route(route, methods=['GET'])
def get_all_unit():
    try:
        units = unit_service.get_all_units()
        if units:
            unit_data = [{"id": unit.id, "name": unit.name} for unit in units]
            return jsonify(unit_data), 200
        else:
            return jsonify({'error': 'Failed to retrieve units'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving units', 'details': str(e)}), 500


@unit_blueprint.route(route + '/<int:unit_id>', methods=['GET'])
def get_unit(unit_id: int):
    try:
        unit = unit_service.get_unit_by_id(unit_id)
        if unit:
            unit_data = {"id": unit.id, "name": unit.name}
            return jsonify(unit_data), 200
        else:
            return jsonify({'error': 'Unit not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the unit', 'details': str(e)}), 500


@unit_blueprint.route(route, methods=['POST'])
def create_unit():
    try:
        data = request.json
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        new_unit = unit_service.create_unit(data['name'])
        if new_unit:
            unit_data = {"id": new_unit.id, "name": new_unit.name}
            return jsonify({'message': 'Unit created successfully', 'unit': unit_data}), 201
        else:
            return jsonify({'error': 'Failed to create unit'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the unit', 'details': str(e)}), 500


@unit_blueprint.route(route + '/<int:unit_id>', methods=['PUT'])
def update_unit(unit_id: int):
    try:
        data = request.json
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid data provided'}), 400

        updated_unit = unit_service.update_unit(unit_id, data['name'])
        if updated_unit:
            unit_data = {"id": updated_unit.id, "name": updated_unit.name}
            return jsonify({'message': 'Unit updated successfully', 'unit': unit_data}), 200
        else:
            return jsonify({'error': 'Unit not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the unit', 'details': str(e)}), 500


@unit_blueprint.route(route + '/<int:unit_id>', methods=['DELETE'])
def delete_unit(unit_id: int):
    try:
        deleted_unit = unit_service.delete_unit(unit_id)
        if deleted_unit:
            unit_data = {"id": deleted_unit.id, "name": deleted_unit.name}
            return jsonify({'message': 'Unit deleted successfully', 'unit': unit_data}), 200
        else:
            return jsonify({'error': 'Unit not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the unit', 'details': str(e)}), 500
