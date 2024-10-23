from flask import Blueprint, request
from service import cliente_service

clientes_routes_blueprint = Blueprint("clientes", __name__)

@clientes_routes_blueprint.route('/clientes', methods=['GET'])
def get_clientes(): 
    return cliente_service.get_clientes()

@clientes_routes_blueprint.route('/clientes/<int:id>', methods=['GET'])
def get_cliente_by_id(id):
    return cliente_service.get_cliente_by_id(id)

@clientes_routes_blueprint.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    return cliente_service.create_cliente(data)

@clientes_routes_blueprint.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    return cliente_service.update_cliente(data, id)

@clientes_routes_blueprint.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    return cliente_service.delete_cliente(id)

# if __name__ == '__main__':
#     app.run(debug=True)
