from flask import Blueprint, request, jsonify
from service.login_service import login_user, register_user

login_routes_blueprint = Blueprint("login", __name__)

@login_routes_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response, status = login_user(data)
    return jsonify(response), status

@login_routes_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response, status = register_user(data)
    return jsonify(response), status