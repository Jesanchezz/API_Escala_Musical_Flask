from marshmallow import Schema, fields

class ResponseMusicalScale(Schema):
    major_musical_scale = fields.List(fields.String(), required= True)
    minor_musical_scale = fields.List(fields.String(), required = True)
    major_pentatonic_musical_scale = fields.List(fields.String(), required = True)
    minor_pentatonic_musical_scale = fields.List(fields.String(), required = True)
    major_blues_musical_scale = fields.List(fields.String(), required = True)
    minor_blues_musical_scale = fields.List(fields.String(), required = True)
