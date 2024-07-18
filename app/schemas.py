from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True, validate=validate.Length(min=1))
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    is_manager = fields.Bool(dump_only=True)

user_schema = UserSchema()