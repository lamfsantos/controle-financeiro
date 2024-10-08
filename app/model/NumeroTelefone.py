from flask_sqlalchemy import SQLAlchemy
from repository.db import db

class PhoneNumer(db.Model):
    id = db.Columsn(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)

    # Foreign Key: links to Client.id
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'), nullable=False)

    def __repr__(self):
        return f"PhoneNumber('{self.number}')"
