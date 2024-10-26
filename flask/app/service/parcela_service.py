from extensions import db
from model import parcela
from flask import jsonify

def get_parcelas():
    parcelas = parcela.parcela.query.all()
    return jsonify([format_parcela(parcela) for parcela in parcelas])

def format_parcela(parcela):
    return {
        'parcela_id': parcela.parcela_id,
        'data_vencimento': parcela.numero_parcela,
        'is_atrasado': parcela.valor_total,
        'processo_id': parcela.valor_entrada
    }

def get_parcela_by_id(id):
    parcela = parcela.parcela.query.get_or_404(id)
    return jsonify(format_parcela(parcela))

def create_parcela(data):
    nova_parcela = parcela.parcela(
        data_vencimento= data['data_vencimento'],
        is_atrasado= data['is_atrasado'],
        processo_id= data['processo_id'],
    )
    db.session.add(nova_parcela)
    db.session.commit()
    return jsonify({
        'parcela_id': nova_parcela.parcela_id,
    }), 201

def update_parcela(data, id):
    parcela = parcela.parcela.query.get_or_404(id)

    parcela.data_vencimento = data.get('data_vencimento', parcela.data_vencimento)
    
    db.session.commit()

    return jsonify({
        'valor_total': parcela.valor_total,
        'valor_entrada': parcela.valor_entrada,
    })

def delete_parcela(id):
    parcela = parcela.parcela.query.get_or_404(id)
    db.session.delete(parcela)
    db.session.commit()
    return '', 204