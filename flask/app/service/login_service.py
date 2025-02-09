from werkzeug.security import check_password_hash
from extensions import db
from model.Usuario import Usuario
import jwt
import datetime

def login_user(data):
    user = Usuario.query.filter_by(login=data['login']).first()
    if user and check_password_hash(user.senha, data['senha']):
        token = jwt.encode({
            'user_id': user.usuario_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, 'secret_key', algorithm='HS256')
        return {'token': token}, 200
    return {'message': 'Invalid credentials'}, 401

def register_user(data):
    new_user = Usuario(login=data['login'], senha=data['senha'])
    print(f"Hashed password: {new_user.senha}")  # Debugging purpose only
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User registered successfully'}, 201
