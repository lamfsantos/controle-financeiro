from flask import Blueprint, request
from service import processo_service

processos_routes_blueprint = Blueprint("processos", __name__)

@processos_routes_blueprint.route('/processos', methods=['GET'])
def get_processos(): 
    return processo_service.get_processos()

@processos_routes_blueprint.route('/processos/<int:id>', methods=['GET'])
def get_processo_by_id(id):
    return processo_service.get_processo_by_id(id)

@processos_routes_blueprint.route('/processos', methods=['POST'])
def create_processo():
    data = request.get_json()
    return processo_service.create_processo(data)

@processos_routes_blueprint.route('/processos/<int:id>', methods=['PUT'])
def update_processo(id):
    data = request.get_json()
    return processo_service.update_processo(data, id)

@processos_routes_blueprint.route('/processos/<int:id>', methods=['DELETE'])
def delete_person(id):
    return processo_service.delete_processo(id)
