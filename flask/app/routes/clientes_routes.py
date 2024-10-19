from flask import Blueprint

clientes_routes_blueprint = Blueprint("cliente", __name__)

@clientes_routes_blueprint.route('/cliente', methods=['GET'])
def get_clientes():
    from service.cliente_service import get_clientes
    return get_clientes()