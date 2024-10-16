from flask import Blueprint


clientes_routes_blueprint = Blueprint("cliente", __name__)


@clientes_routes_blueprint.route('/cliente', methods=['GET'])
def get_clientes():
    return "clientes"