from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from typing import List
from schemas.KeySchema import KeyModel
from schemas.ResponseMusicalScaleShema import ResponseMusicalScale
from musical_scale_module.MusicalScale import MusicalScale

musical_scale_bp = Blueprint("musical_scale_bp", __name__)

MUSICAL_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E','F','F#','G','G#']

ms = MusicalScale()

def request_note(musical_scale:List[str], key:str):
    if key.islower():
        key = key.upper()

    elif key not in musical_scale:
        return jsonify({"msg":"No existe esa nota."}),404

    index = musical_scale.index(key)

    return jsonify({"index":index,
            "key":key})

@musical_scale_bp.route("/", methods = ["POST"])
def create_scale_musical():
    data = request.get_json()
    
    schema = KeyModel()

    try:
        validated_key = schema.load(data)
        print(validated_key)
    except ValidationError as err:
        return jsonify({"ERROR":err.messages}), 400
    
    response_note = request_note(MUSICAL_SCALE, validated_key["key"])

    response_index = response_note.get_json()["index"]

    accommodated_scale = ms.accommodate_scale(MUSICAL_SCALE, response_index)
    major_scale = ms.create_major_scale(accommodated_scale.copy())
    minor_scale = ms.create_minor_scale(accommodated_scale.copy())
    major_pentatonic_scale = ms.create_major_pentatonic_scale(major_scale.copy())
    minor_pentatonic_scale = ms.create_minor_pentatonic_scale(minor_scale.copy())
    major_blues_scale = ms.create_major_blues_scale(MUSICAL_SCALE, major_pentatonic_scale.copy())
    minor_blues_scale = ms.create_minor_blues_scale(MUSICAL_SCALE, minor_pentatonic_scale.copy())


    response_schema_musical_scale = ResponseMusicalScale()

    response_data = {
        "major_musical_scale": major_scale,
        "minor_musical_scale": minor_scale,
        "major_pentatonic_musical_scale": major_pentatonic_scale,
        "minor_pentatonic_musical_scale": minor_pentatonic_scale,
        "major_blues_musical_scale": major_blues_scale,
        "minor_blues_musical_scale": minor_blues_scale
    }
    
    result = response_schema_musical_scale.dump(response_data)

    return jsonify(result)