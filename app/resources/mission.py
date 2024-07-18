from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import db, Mission
from app.schemas import mission_schema, missions_schema

bp = Blueprint('missions', __name__, url_prefix='/missions')

@bp.route('/', methods=['POST'])
@jwt_required()
def create_mission():
    data = request.get_json()
    errors = mission_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    mission = Mission(
        name=data['name'], 
        description=data.get('description'), 
        user_id=data['user_id']
    )
    db.session.add(mission)
    db.session.commit()

    return mission_schema.jsonify(mission), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def get_missions():
    missions = Mission.query.all()
    return missions_schema.jsonify(missions), 200