class Cliente {
  final int cliente_id;
  final String nome;
  final String endereco;
  final String cpf;
  final String rg;
  final String email;
  final String telefone_principal;
  final String telefone_secundario;
  final String observacoes;

  Cliente(
      {required this.cliente_id,
      required this.nome,
      required this.endereco,
      required this.cpf,
      required this.rg,
      required this.email,
      required this.telefone_principal,
      required this.telefone_secundario,
      required this.observacoes});

  factory Cliente.fromJson(Map<String, dynamic> json) {
    return Cliente(
      cliente_id: json['cliente_id'],
      nome: json['nome'],
      endereco: json['endereco'],
      cpf: json['cpf'],
      rg: json['rg'],
      email: json['email'],
      telefone_principal: json['telefone_principal'],
      telefone_secundario: json['telefone_secundario'],
      observacoes: json['observacoes'],
    );
  }
}
