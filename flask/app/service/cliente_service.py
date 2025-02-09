from extensions import db
from model import Cliente
from flask import jsonify

def get_clientes():
    clientes = Cliente.Cliente.query.all()
    return jsonify([format_cliente(cliente) for cliente in clientes])

def get_cliente_by_id(id):
    cliente = Cliente.Cliente.query.get_or_404(id)
    return jsonify(format_cliente(cliente))

def format_cliente(cliente):
    return {
        'cliente_id': cliente.cliente_id,
        'nome': cliente.nome,
        'endereco': cliente.endereco,
        'cpf': cliente.cpf,
        'rg': cliente.rg,
        'email': cliente.email,
        'telefone_principal': cliente.telefone_principal,
        'telefone_secundario': cliente.telefone_secundario,
        'observacoes': cliente.observacoes,
        'processos': [
            {
                'processo_id': processo.processo_id, 
                'valor_total': processo.valor_total, 
                'valor_entrada': processo.valor_entrada, 
                'numero_processo': processo.numero_processo
            } for processo in cliente.processos
        ]
    }

def create_cliente(data):
    novo_cliente = Cliente.Cliente(
        nome= data['nome'],
        endereco= data['endereco'],
        cpf= data['cpf'],
        rg= data['rg'],
        email= data['email'],
        telefone_principal= data['telefone_principal'],
        telefone_secundario= data['telefone_secundario'],
        observacoes= data['observacoes']
    )
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({
        'cliente_id': novo_cliente.cliente_id,
        'nome': novo_cliente.nome,
    }), 201

def update_cliente(data, id):
    cliente = Cliente.Cliente.query.get_or_404(id)

    cliente.nome = data.get('nome', cliente.nome)
    cliente.endereco = data.get('endereco', cliente.endereco)
    cliente.cpf = data.get('cpf', cliente.cpf)
    cliente.rg = data.get('rg', cliente.rg)
    cliente.email = data.get('email', cliente.email)
    cliente.telefone_principal = data.get('telefone_principal', cliente.telefone_principal)
    cliente.telefone_secundario = data.get('telefone_secundario', cliente.telefone_secundario)
    cliente.observacoes = data.get('observacoes', cliente.observacoes)

    db.session.commit()

    return jsonify({
        'cliente_id': cliente.cliente_id,
        'nome': cliente.nome,
    })

def delete_cliente(id):
    cliente = Cliente.Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return '', 204

    