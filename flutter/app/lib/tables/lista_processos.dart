import 'package:flutter/material.dart';

class ListaProcessosTable extends StatefulWidget {
  final List<Map<String, String>> otherInfo;

  ListaProcessosTable({required this.otherInfo});

  @override
  _OtherInfoTableState createState() => _OtherInfoTableState();
}

class _OtherInfoTableState extends State<ListaProcessosTable> {
  late List<Map<String, String>> otherInfo;

  @override
  void initState() {
    super.initState();
    otherInfo = widget.otherInfo;
  }

  void updateInfo(String key, String value) {
    setState(() {
      int index = otherInfo.indexWhere((info) => info['key'] == key);
      if (index != -1) {
        otherInfo[index]['value'] = value;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return DataTable(
      columns: const <DataColumn>[
        DataColumn(label: Text('Key')),
        DataColumn(label: Text('Value')),
      ],
      rows: otherInfo
          .map((info) => DataRow(cells: [
                DataCell(Text(info['key'] ?? 'aaa')),
                DataCell(Text(info['value'] ?? 'aaa')),
              ]))
          .toList(),
    );
  }
}
