from flask import Blueprint, request
from service import processo_service

processos_routes_blueprint = Blueprint("processos", __name__)

@processos_routes_blueprint.route('/processos', methods=['GET'])
def get_processos(): 
    return processo_service.get_processos()