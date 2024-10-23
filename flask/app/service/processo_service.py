from extensions import db
from model import Processo
from flask import jsonify

def get_processos():
    processos = Processo.Processo.query.all()
    return jsonify([format_processo(processo) for processo in processos])

def format_processo(processo):
    return {
        'processo_id': processo.processo_id,
        'numero_processo': processo.numero_processo,
        'valor_total': processo.valor_total,
        'valor_entrada': processo.valor_entrada,
        'cliente_id': processo.cliente_id
    }

def get_processo_by_id(id):
    processo = Processo.Processo.query.get_or_404(id)
    return jsonify(format_processo(processo))

def create_processo(data):
    novo_processo = Processo.Processo(
        valor_total= data['valor_total'],
        valor_entrada= data['valor_entrada'],
        cliente_id= data['cliente_id'],
    )
    db.session.add(novo_processo)
    db.session.commit()
    return jsonify({
        'processo_id': novo_processo.processo_id,
    }), 201

def update_processo(data, id):
    processo = Processo.Processo.query.get_or_404(id)

    processo.valor_total = data.get('valor_total', processo.valor_total)
    processo.valor_entrada = data.get('valor_entrada', processo.valor_entrada)
    
    db.session.commit()

    return jsonify({
        'valor_total': processo.valor_total,
        'valor_entrada': processo.valor_entrada,
    })

def delete_processo(id):
    processo = Processo.Processo.query.get_or_404(id)
    db.session.delete(processo)
    db.session.commit()
    return '', 204