from model.Cliente import Cliente
from flask import jsonify

@app.route('/cliente', methods=['GET'])
def get_persons():
    clientes = Cliente.query.all()
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