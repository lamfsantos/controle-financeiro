from extensions import db

class Usuario(db.Model):
    usuario_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)