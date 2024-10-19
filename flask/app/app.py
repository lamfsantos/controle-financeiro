from flask import Flask
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@mysql/controle_financeiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize the SQLAlchemy object
db.init_app(app)

def inicializa_blueprints():
    try:
        from routes.clientes_routes import clientes_routes_blueprint

        print("Registrnado Blueprints...")

        # Blueprints
        app.register_blueprint(clientes_routes_blueprint)

        print("Blueprints registrados.")
    except Exception as e:
        print(f"Erro ao inicializar os Blueprints: {e}")
    

inicializa_blueprints()

# Create the database and tables
with app.app_context():
    print("Criando DB...")
    try:
        db.create_all()
        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao criar as tabelas do banco: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
