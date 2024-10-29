import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert'; // Add this line
import 'teste.dart';
import 'package:controle_financeiro/config.dart';

class ClienteForm extends StatefulWidget {
  @override
  _ClienteFormState createState() => _ClienteFormState();
}

class _ClienteFormState extends State<ClienteForm> {
  final _formKey = GlobalKey<FormState>();
  String _nome = '';
  String _endereco = '';
  String _cpf = '';
  String _rg = '';
  String _email = '';
  String _telefone_principal = '';
  String _telefone_secundario = '';
  String _observacoes = '';

  void _submit() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      final response = await http.post(
        Uri.parse('${Config.flask_url}/clientes'), // Replace with your API host
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'nome': _nome,
          'endereco': _endereco,
          'cpf': _cpf,
          'rg': _rg,
          'email': _email,
          'telefone_principal': _telefone_principal,
          'telefone_secundario': _telefone_secundario,
          'observacoes': _observacoes,
        }),
      );
      if (response.statusCode == 201) {
        // Handle successful response
        print('Cliente added: $_nome');
      } else {
        // Handle error response
        print('Failed to add cliente');
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Cliente'),
      ),
      body: Center(
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 20),
          constraints: BoxConstraints(maxWidth: 600),
          child: Form(
            key: _formKey,
            autovalidateMode: AutovalidateMode.onUserInteraction,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                //SizedBox(height: 100), // Add space at the top
                TextFormField(
                  decoration: InputDecoration(labelText: 'Nome'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um nome';
                    }
                    return null;
                  },
                  onSaved: (value) => _nome = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Endereço'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um Endereço';
                    }
                    return null;
                  },
                  onSaved: (value) => _endereco = value!,
                ),
                // Add other TextFormField widgets here
                TextFormField(
                  decoration: InputDecoration(labelText: 'CPF'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um CPF';
                    }
                    return null;
                  },
                  onSaved: (value) => _cpf = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'RG'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um RG';
                    }
                    return null;
                  },
                  onSaved: (value) => _rg = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Email'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um Email';
                    }
                    return null;
                  },
                  onSaved: (value) => _email = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Telefone Principal'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um Telefone Principal';
                    }
                    return null;
                  },
                  onSaved: (value) => _telefone_principal = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Telefone Secundário'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um Telefone Secundário';
                    }
                    return null;
                  },
                  onSaved: (value) => _telefone_secundario = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Observações'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite Observações';
                    }
                    return null;
                  },
                  onSaved: (value) => _observacoes = value!,
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: _submit,
                  child: Text('Submit'),
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => SecondScreen()),
                    );
                  },
                  child: Text('Go to Second Screen'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
