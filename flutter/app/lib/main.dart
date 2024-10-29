import 'package:flutter/material.dart';
//import 'forms/cadastra_cliente_form.dart';
import 'public/login.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Controle Financeiro', home: Login() //ClienteForm(),
        );
  }
}
