from extensions import db

class Processo(db.Model):
    processo_id = db.Column(db.Integer, primary_key=True)
    numero_processo = db.Column(db.String(50), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    valor_entrada = db.Column(db.Float)

    # Foreign Key: links to Client.id
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'), nullable=False)
