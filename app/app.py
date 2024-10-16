# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financeiro.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)

def inicializa_blueprints():
    from routes.clientes_routes import clientes_routes_blueprint

    # Blueprints
    app.register_blueprint(clientes_routes_blueprint)

inicializa_blueprints()

# Initialize the SQLAlchemy object
#db.init_app(app)

# Create the database and tables

if __name__ == '__main__':
    with app.app_context():
        print("Criando DB...")
        try:
            from model import Cliente
            db.create_all()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar as tabelas do banco: {e}")

    app.run(host='0.0.0.0', port=5000)
