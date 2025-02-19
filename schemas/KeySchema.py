from marshmallow import Schema, fields

class KeyModel(Schema):
    key = fields.Str(required=True, error_messages={"required": "Se necesita un acorde de la escala musical."})