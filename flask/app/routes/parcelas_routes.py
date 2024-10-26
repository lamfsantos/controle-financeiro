from flask import Blueprint, request
from service import parcela_service

parcelas_routes_blueprint = Blueprint("parcelas", __name__)

@parcelas_routes_blueprint.route('/parcelas', methods=['GET'])
def get_parcelas(): 
    return parcela_service.get_parcelas()

@parcelas_routes_blueprint.route('/parcelas/<int:id>', methods=['GET'])
def get_parcela_by_id(id):
    return parcela_service.get_parcela_by_id(id)

@parcelas_routes_blueprint.route('/parcelas', methods=['POST'])
def create_parcela():
    data = request.get_json()
    return parcela_service.create_parcela(data)

@parcelas_routes_blueprint.route('/parcelas/<int:id>', methods=['PUT'])
def update_parcela(id):
    data = request.get_json()
    return parcela_service.update_parcela(data, id)

@parcelas_routes_blueprint.route('/parcelas/<int:id>', methods=['DELETE'])
def delete_person(id):
    return parcela_service.delete_parcela(id)
