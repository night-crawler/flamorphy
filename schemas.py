from marshmallow import Schema, fields


class OpencorporaTagSchema(Schema):
    animacy = fields.Str()
    aspect = fields.Str()
    case = fields.Str()
    cyr_repr = fields.Str()
    gender = fields.Str()
    involvement = fields.Str()
    mood = fields.Str()
    number = fields.Str()
    person = fields.Str()
    tense = fields.Str()
    transitivity = fields.Str()
    voice = fields.Str()
    grammemes = fields.List(fields.Str())
    grammemes_cyr = fields.List(fields.Str())


class PyMorphyParseResultSchemaLight(Schema):
    score = fields.Float()
    word = fields.Str()
    normal_form = fields.Str()
    is_known = fields.Bool()
    tag = fields.Nested(OpencorporaTagSchema)


class PyMorphyParseResultSchema(PyMorphyParseResultSchemaLight):
    normalized = fields.Nested(PyMorphyParseResultSchemaLight)
    lexeme = fields.List(fields.Nested(PyMorphyParseResultSchemaLight))


# class PyMorphySchema(Schema):
