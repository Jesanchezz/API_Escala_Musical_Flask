from marshmallow import Schema, validates, fields, ValidationError

VALID_NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

class KeyModel(Schema):
    
    key = fields.String(required=True)
    
    @validates("key")
    def validate_note(self, value):
        value_upper= value.upper()
        
        if value_upper not in VALID_NOTES:
            raise ValidationError("Nota incorrecta. Por favor ingrese una nota válida (ejemplo: 'C', 'A#', 'G').")
