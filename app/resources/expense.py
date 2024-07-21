from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import db, Expense
from app.schemas import expense_schema, expenses_schema
from datetime import datetime

bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@bp.route('/', methods=['POST'])
@jwt_required()
def create_expense():
    data = request.get_json()
    errors = expense_schema.validate(data)
    if errors:
        print(errors)
        return jsonify(errors), 400

    try:
        date_obj = datetime.strptime(data['date'], '%Y-%m-%d').date()
    except ValueError as e:
        return jsonify({'date': str(e)}), 400

    expense = Expense(
        amount=data['amount'],
        description=data.get('description'),
        date=date_obj,
        mission_id=data['mission_id']
    )
    db.session.add(expense)
    db.session.commit()

    result = expense_schema.dump(expense)
    return jsonify(result), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def get_expenses():
    expenses = Expense.query.all()
    result = expenses_schema.dump(expenses)
    return jsonify(result), 200