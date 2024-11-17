class Processo {
  final int processo_id;
  final double valor_total;
  final double valor_entrada;
  final String numero_processo;

  Processo({
    required this.processo_id,
    required this.valor_total,
    required this.valor_entrada,
    required this.numero_processo,
  });

  factory Processo.fromJson(Map<String, dynamic> json) {
    return Processo(
      processo_id: json['processo_id'] ?? 0,
      valor_total: json['valor_total'] ?? 0.0,
      valor_entrada: json['valor_entrada'] ?? 0.0,
      numero_processo: json['numero_processo'] ?? '',
    );
  }
}
