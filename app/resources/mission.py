from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
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
    current_user_id = get_jwt_identity()
    mission = Mission(
        name=data['name'], 
        description=data.get('description'), 
        user_id=current_user_id
    )
    db.session.add(mission)
    db.session.commit()

    result = mission_schema.dump(mission)
    return jsonify(result), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def get_missions():
    missions = Mission.query.all()
    result = missions_schema.dump(missions)
    return jsonify(result), 200