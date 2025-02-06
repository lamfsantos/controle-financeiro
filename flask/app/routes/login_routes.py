from flask import Blueprint, request
#from service import cliente_service

clientes_routes_blueprint = Blueprint("login", __name__)

@clientes_routes_blueprint.route('/login', methods=['GET'])
def get_clientes(): 
    return ""