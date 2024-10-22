from extensions import db
from model import Processo
from flask import jsonify

def get_processos():
    processos = Processo.Processo.query.all()
    return jsonify([format_processo(processo) for processo in processos])

def format_processo(Processo):
    return {
        'processo_id': processo.processo_id,
        'valor_total': processo.valor_total,
        'valor_entrada': processo.valor_entrada,
        'cliente_id': processo.cliente_id
    }