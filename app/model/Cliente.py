from repository.db import db

class Cliente(db.Model):
    cliente_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50))
    telefone_principal
    telefone_secundario
    observacoes

    def __repr__(self):
        return f"User('{self.nome}', '{self.email}')"