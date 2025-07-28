from flask import Blueprint, request, jsonify
from .models import User
from .database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Microsserviço está funcionando!'

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])
