import 'package:flutter/material.dart';

import '../model/processo.dart';

class ListaProcessosTable extends StatefulWidget {
  final List<Processo> processos;

  ListaProcessosTable({required this.processos});

  @override
  _ListaProcessosTableState createState() => _ListaProcessosTableState();
}

class _ListaProcessosTableState extends State<ListaProcessosTable> {
  late List<Processo> processos;

  @override
  void initState() {
    super.initState();
    processos = widget.processos;
  }

  void updateProcesso(int processoId, double valorEntrada) {
    setState(() {
      int index = processos.indexWhere((processo) => processo.processo_id == processoId);
      if (index != -1) {
        processos[index] = Processo(
          processo_id: processos[index].processo_id,
          valor_total: processos[index].valor_total,
          valor_entrada: valorEntrada,
          numero_processo: processos[index].numero_processo,
        );
      }
    });

    for (var x in processos) {
      print(x.processo_id);
    }
  }

  @override
  Widget build(BuildContext context) {
    return DataTable(
      columns: const <DataColumn>[
        DataColumn(label: Text('Processo ID')),
        DataColumn(label: Text('Valor Total')),
        DataColumn(label: Text('Valor Entrada')),
        DataColumn(label: Text('Número Processo')),
      ],
      rows: processos
          .map((processo) => DataRow(cells: [
                DataCell(Text(processo.processo_id.toString())),
                DataCell(Text(processo.valor_total.toString())),
                DataCell(Text(processo.valor_entrada.toString())),
                DataCell(Text(processo.numero_processo.toString())),
              ]))
          .toList(),
    );
  }
}
