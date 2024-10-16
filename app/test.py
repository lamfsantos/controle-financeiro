# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configuration for SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # Define the Person model
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<Person {self.name}>'

# # Create the database and tables
# with app.app_context():
#     db.create_all()

# # CRUD Routes
# @app.route('/persons', methods=['GET'])
# def get_persons():
#     persons = Person.query.all()
#     return jsonify([{
#         'id': person.id,
#         'name': person.name,
#         'age': person.age,
#         'email': person.email
#     } for person in persons])

# @app.route('/person/<int:id>', methods=['GET'])
# def get_person(id):
#     person = Person.query.get_or_404(id)
#     return jsonify({
#         'id': person.id,
#         'name': person.name,
#         'age': person.age,
#         'email': person.email
#     })

# @app.route('/person', methods=['POST'])
# def create_person():
#     data = request.get_json()
#     new_person = Person(
#         name=data['name'],
#         age=data['age'],
#         email=data['email']
#     )
#     db.session.add(new_person)
#     db.session.commit()
#     return jsonify({
#         'id': new_person.id,
#         'name': new_person.name,
#         'age': new_person.age,
#         'email': new_person.email
#     }), 201

# @app.route('/person/<int:id>', methods=['PUT'])
# def update_person(id):
#     data = request.get_json()
#     person = Person.query.get_or_404(id)
#     person.name = data.get('name', person.name)
#     person.age = data.get('age', person.age)
#     person.email = data.get('email', person.email)
#     db.session.commit()
#     return jsonify({
#         'id': person.id,
#         'name': person.name,
#         'age': person.age,
#         'email': person.email
#     })

# @app.route('/person/<int:id>', methods=['DELETE'])
# def delete_person(id):
#     person = Person.query.get_or_404(id)
#     db.session.delete(person)
#     db.session.commit()
#     return '', 204

# if __name__ == '__main__':
#     app.run(debug=True)
