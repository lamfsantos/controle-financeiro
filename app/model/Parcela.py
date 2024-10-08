from flask_sqlalchemy import SQLAlchemy
from repository.db import db

class Parcela(db.Model):
    parcela_id = db.Column(db.Integer, primary_key=True)
    data_vencimento = db.Column(db.Date, nullable=False)
    is_atrasado = db.Column(db.Boolean, nullable=False)
    juros

    # Foreign Key: links to Client.id
    processo_id = db.Column(db.Integer, db.ForeignKey('processo.processo_id'), nullable=False)