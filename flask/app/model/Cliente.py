from extensions import db

class Cliente(db.Model):
    cliente_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    rg = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50))
    telefone_principal = db.Column(db.String(15), nullable=False)
    telefone_secundario = db.Column(db.String(15))
    observacoes = db.Column(db.String(200), nullable=False)

    processos = db.relationship('Processo', backref='cliente', lazy=True)