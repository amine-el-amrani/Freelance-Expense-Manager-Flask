from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import db, Expense
from app.schemas import expense_schema, expenses_schema

bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@bp.route('/', methods=['POST'])
@jwt_required()
def create_expense():
    data = request.get_json()
    errors = expense_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    expense = Expense(
        amount=data['amount'], 
        description=data.get('description'), 
        date=data['date'],
        mission_id=data['mission_id']
    )
    db.session.add(expense)
    db.session.commit()

    return expense_schema.jsonify(expense), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def get_expenses():
    expenses = Expense.query.all()
    return expenses_schema.jsonify(expenses), 200