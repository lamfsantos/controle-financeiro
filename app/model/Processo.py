from repository.db import db

class Processo(db.Model):
    processo_id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float, nullable=False)
    valor_entrada = db.Column(db.Float)

    # Foreign Key: links to Client.id
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'), nullable=False)
