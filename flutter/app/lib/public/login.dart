import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
//import '/forms/cadastra_cliente_form.dart';
import '/tables/lista_clientes.dart';

class LoginForm extends StatefulWidget {
  @override
  _LoginFormState createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  //Declaração de variáveis
  final _formKey = GlobalKey<FormState>();
  String _login = '';
  String _senha = '';

  //Declaração função submit

  void _submit() async {
    //Bloco de código para teste, só precisa descomentar quando for implementar 
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      //   final response = await http.post(
      //     //condition here
      //   )
      print(_login);
      print(_senha);

      Navigator.push(
          context, MaterialPageRoute(builder: (context) => ClientesPage()));
    }

    // Base do sistema de Login, só precisa descomentar quando for implementar e 
    // deletar o bloco de código acima

    // if (_formKey.currentState!.validate()) {
    //   _formKey.currentState!.save();
    //   final response = await http.post(
    //     Uri.parse('http://localhost:5000/login'),
    //     headers: <String, String>{
    //       'Content-Type': 'application/json; charset=UTF-8',
    //     },
    //     body: jsonEncode(<String, String>{
    //       'login': _login,
    //       'senha': _senha,
    //     }),
    //   );

    //   if (response.statusCode == 200) {
    //     Navigator.push(
    //         context, MaterialPageRoute(builder: (context) => ClientesPage()));
    //   } else {
    //     // Handle login failure
    //     ScaffoldMessenger.of(context).showSnackBar(
    //       SnackBar(content: Text('Login failed')),
    //     );
    //   }
    // }
  }

  //Build da parada

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Login'),
      ),
      body: Center(
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 50),
          constraints: BoxConstraints(maxWidth: 600),
          child: Form(
            key: _formKey,
            autovalidateMode: AutovalidateMode.onUserInteraction,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                TextFormField(
                  decoration: InputDecoration(
                    labelText: 'Login',
                  ),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite um login';
                    }
                    return null;
                  },
                  onSaved: (value) => _login = value!,
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Senha'),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Por favor digite uma senha';
                    }
                    return null;
                  },
                  onSaved: (value) => _senha = value!,
                ),
                SizedBox(height: 20),
                ElevatedButton(onPressed: _submit, child: Text('Entra')),
                SizedBox(height: 50),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
