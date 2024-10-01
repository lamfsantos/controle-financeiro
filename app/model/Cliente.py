from flask_sqlalchemy import SQLAlchemy
from repository.db import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)

    
    lista_telefones
    lista_processos
    pass

# def __repr__(self):
        # return f"User('{self.nome}', '{self.email}')"