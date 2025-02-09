from extensions import db
from werkzeug.security import generate_password_hash

class Usuario(db.Model):
    usuario_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __init__(self, login, senha):
        self.login = login
        self.senha = generate_password_hash(senha)