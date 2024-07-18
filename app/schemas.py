from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True, validate=validate.Length(min=1))
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    is_manager = fields.Bool(dump_only=True)

user_schema = UserSchema()

class MissionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str()
    user_id = fields.Int(dump_only=True)

mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    description = fields.Str()
    date = fields.Date(required=True)
    mission_id = fields.Int(dump_only=True)

expense_schema = ExpenseSchema()
expenses_schema = ExpenseSchema(many=True)
