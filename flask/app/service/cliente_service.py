from app import db
from model import Cliente
from flask import jsonify

def get_clientes():
    clientes = Cliente.Cliente.query.all()
    return jsonify([{
        'cliente_id': cliente.cliente_id,
        'nome': cliente.nome,
        'endereco': cliente.endereco,
        'cpf': cliente.cpf,
        'rg': cliente.rg,
        'email': cliente.email,
        'telefone_principal': cliente.telefone_principal,
        'telefone_secundario': cliente.telefone_secundario,
        'observacoes': cliente.observacoes
    } for cliente in clientes])