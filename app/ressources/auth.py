from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from app.models import db, User
from app.schemas import user_schema

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'error': 'User already exists'}), 400
    user = User(
        username=data['username'], 
        email=data['email'], 
        password_hash=generate_password_hash(data['password']))
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 400

    token = create_access_token(identity=user.id)
    return jsonify({'token': token}), 200