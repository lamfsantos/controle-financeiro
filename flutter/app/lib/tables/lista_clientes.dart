import 'package:flutter/material.dart';
import 'dart:convert'; // For decoding JSON
import 'package:http/http.dart' as http; // Add http dependency
import 'package:controle_financeiro/config.dart';
import 'package:controle_financeiro/forms/cadastra_cliente_form.dart';
import 'package:controle_financeiro/model/cliente.dart';
import 'package:controle_financeiro/edit/cliente_info.dart';

class ClientesPage extends StatefulWidget {
  @override
  _ClientesPageState createState() => _ClientesPageState();
}

class _ClientesPageState extends State<ClientesPage> {
  late Future<List<Cliente>> clientes;

  @override
  void initState() {
    super.initState();
    clientes = fetchClientes();
  }

  Future<List<Cliente>> fetchClientes() async {
    final response = await http.get(Uri.parse('${Config.flask_url}/clientes'));
    if (response.statusCode == 200) {
      List jsonResponse = json.decode(response.body);
      return jsonResponse.map((cliente) => Cliente.fromJson(cliente)).toList();
    } else {
      throw Exception('Failed to load clientes');
    }
  }

  void _navigateToClientInfoPage(
      BuildContext context, List<Cliente> clientes, int clientId) {
    Cliente? selectedClient = clientes.firstWhere(
      (cliente) => cliente.cliente_id == clientId,
      orElse: () => Cliente(
        cliente_id: 0,
        nome: 'Unknown',
        email: '',
        cpf: '',
        endereco: '',
        observacoes: '',
        rg: '',
        telefone_principal: '',
        telefone_secundario: '',
      ),
    );
    if (selectedClient.cliente_id != 0) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ClientInfoPage(cliente: selectedClient),
        ),
      );
    } else {
      print('Cliente não encontrado');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Clientes'),
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 50),
          constraints: BoxConstraints(maxWidth: 600),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              FutureBuilder<List<Cliente>>(
                future: clientes,
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return Center(child: CircularProgressIndicator());
                  } else if (snapshot.hasError) {
                    return Center(child: Text('Error: ${snapshot.error}'));
                  } else {
                    return DataTable(
                      columns: const <DataColumn>[
                        DataColumn(label: Text('Nome')),
                        //DataColumn(label: Text('Endereço')),
                        //DataColumn(label: Text('CPF')),
                        //DataColumn(label: Text('RG')),
                        //DataColumn(label: Text('Email')),
                        //DataColumn(label: Text('Telefone 1')),
                        //DataColumn(label: Text('Telefone 2')),
                        //DataColumn(label: Text('Observações')),
                        DataColumn(label: Text('Opções')),
                      ],
                      rows: snapshot.data!
                          .map((cliente) => DataRow(cells: [
                                DataCell(Text(cliente.nome)),
                                //DataCell(Text(cliente.endereco)),
                                //DataCell(Text(cliente.cpf)),
                                //DataCell(Text(cliente.rg)),
                                //DataCell(Text(cliente.email)),
                                //DataCell(Text(cliente.telefone_principal)),
                                //DataCell(Text(cliente.telefone_secundario)),
                                //DataCell(Text(cliente.observacoes)),

                                // DataCell(),
                                // DataCell(ElevatedButton(
                                //     onPressed: _teste_botoes,
                                //     child: Text('Processos'))),
                                DataCell(Row(
                                  children: [
                                    IconButton(
                                        onPressed: () =>
                                            _navigateToClientInfoPage(
                                                context,
                                                snapshot.data!,
                                                cliente.cliente_id),
                                        color: Colors.blue,
                                        icon: Icon(Icons.arrow_forward)),
                                  ],
                                )),
                              ]))
                          .toList(),
                    );
                  }
                },
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
              context, MaterialPageRoute(builder: (context) => ClienteForm()));
        },
        child: Icon(Icons.add),
        tooltip: 'Add',
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
    );
  }
}
