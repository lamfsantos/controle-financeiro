import 'package:controle_financeiro/tables/lista_processos.dart';
import 'package:flutter/material.dart';
import 'package:controle_financeiro/model/cliente.dart';

class ClientInfoPage extends StatefulWidget {
  final Cliente cliente;

  ClientInfoPage({required this.cliente});

  @override
  _ClientInfoPageState createState() => _ClientInfoPageState();
}

class _ClientInfoPageState extends State<ClientInfoPage> {
  bool isEditing = false;
  late TextEditingController nomeController;
  late TextEditingController enderecoController;
  late TextEditingController cpfController;
  late TextEditingController addressController;
  late TextEditingController rgController;
  late TextEditingController emailController;
  late TextEditingController telefonePrincipalController;
  late TextEditingController telefoneSecundarioController;
  late TextEditingController observacoesController;

  //Teste - remover depois
  List<Map<String, String>> otherInfo = [
    {'key': 'Additional Info 1', 'value': 'Value 1'},
    {'key': 'Additional Info 2', 'value': 'Value 2'},
  ];

  @override
  void initState() {
    super.initState();
    nomeController = TextEditingController(text: widget.cliente.nome);
    enderecoController = TextEditingController(text: widget.cliente.endereco);
    cpfController = TextEditingController(text: widget.cliente.cpf);
    rgController = TextEditingController(text: widget.cliente.rg);
    emailController = TextEditingController(text: widget.cliente.email);
    telefonePrincipalController =
        TextEditingController(text: widget.cliente.telefone_principal);
    telefoneSecundarioController =
        TextEditingController(text: widget.cliente.telefone_secundario);
    observacoesController =
        TextEditingController(text: widget.cliente.observacoes);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Informações do Cliente'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            CustomTextField(
              controller: nomeController,
              labelText: 'Nome',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: enderecoController,
              labelText: 'Endereço',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: cpfController,
              labelText: 'CPF',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: rgController,
              labelText: 'RG',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: emailController,
              labelText: 'Email',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: telefonePrincipalController,
              labelText: 'Telefone 1',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: telefoneSecundarioController,
              labelText: 'Telefone 2',
              isEditing: isEditing,
            ),
            SizedBox(height: 10),
            CustomTextField(
              controller: observacoesController,
              labelText: 'Observações',
              isEditing: isEditing,
            ),
            SizedBox(height: 20),
            if (isEditing) ...[
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton(
                    onPressed: () {
                      setState(() {
                        isEditing = false;
                      });
                      // Add your save logic here
                    },
                    child: Text('OK'),
                  ),
                  ElevatedButton(
                    onPressed: () {
                      setState(() {
                        isEditing = false;
                      });
                      // Add your cancel logic here
                    },
                    child: Text('Cancela'),
                  ),
                ],
              ),
            ] else ...[
              ElevatedButton(
                onPressed: () {
                  setState(() {
                    isEditing = true;
                  });
                },
                child: Text('Editar'),
              ),
            ],
            SizedBox(height: 50),
            ListaProcessosTable(otherInfo: otherInfo),
          ],
        ),
      ),
    );
  }
}

class CustomTextField extends StatelessWidget {
  final TextEditingController controller;
  final String labelText;
  final bool isEditing;

  CustomTextField({
    required this.controller,
    required this.labelText,
    required this.isEditing,
  });

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: controller,
      decoration: InputDecoration(
        labelText: labelText,
        filled: true,
        fillColor: isEditing ? Colors.white : Colors.grey[300],
      ),
      readOnly: !isEditing,
    );
  }
}
