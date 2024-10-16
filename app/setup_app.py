from flask import Flask
from routes.clietes_routes import clientes_routes_blueprint

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Blueprints
app.register_blueprint(clientes_routes_blueprint)