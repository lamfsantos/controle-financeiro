from flask_sqlalchemy import SQLAlchemy
from repository.db import db

class Process(db.Model):
    valor_total
    entrada
    data_de_vencimento

    
    numero_de_parcelas
    valor_parcelas

    pass