from flask import Flask, request, jsonify
from flask_migrate import Migrate# type: ignore
from flask_cors import CORS # type: ignore
from extensions import db
import jwt # type: ignore

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:8000", "http://127.0.0.1:5555", "http://localhost:5555"]}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@mysql/controle_financeiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize the SQLAlchemy object
db.init_app(app)
migrate = Migrate(app, db)

@app.before_request
def handle_options_requests():
    if request.method == 'OPTIONS':
        return '', 200

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            jwt.decode(token, 'secret_key', algorithms=['HS256'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorator

def inicializa_blueprints():
    try:
        from routes.clientes_routes import clientes_routes_blueprint
        from routes.processos_routes import processos_routes_blueprint
        #Base do sistema de Login
        #from routes.login_routes import login_routes_blueprint

        print("Registrando Blueprints...")

        # Blueprints
        app.register_blueprint(clientes_routes_blueprint)
        app.register_blueprint(processos_routes_blueprint)
        #Base do sistema de Login
        #app.register_blueprint(login_routes_blueprint, url_prefix='/auth')  # Ensure the URL prefix is correct

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
