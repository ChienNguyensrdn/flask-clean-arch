from marshmallow import Schema, fields

class TodoSchema(Schema):
    id = fields.Int(required=True)
    task = fields.Str(required=True)
    completed = fields.Bool(load_default=False)