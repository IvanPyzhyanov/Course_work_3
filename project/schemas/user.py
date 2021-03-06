from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre_id = fields.Int()