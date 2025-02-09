from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from extensions import db
from model.Usuario import Usuario
import jwt
import datetime

login_routes_blueprint = Blueprint("login", __name__)

@login_routes_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Usuario.query.filter_by(login=data['login']).first()
    if user and check_password_hash(user.senha, data['senha']):
        token = jwt.encode({
            'user_id': user.usuario_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, 'secret_key', algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@login_routes_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = Usuario(login=data['login'], senha=data['senha'])
    print(f"Hashed password: {new_user.senha}")  # Debugging purpose only
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201