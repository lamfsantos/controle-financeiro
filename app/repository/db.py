from flask_sqlalchemy import SQLAlchemy
from setup_app import app

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Create the database and tables
with app.app_context():
    db.create_all()