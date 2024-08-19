import marshmallow
from marshmallow import fields, validate


class BurgerSchema(marshmallow.Schema):
    bread = fields.Str(required=True, validate=[validate.Length(min=1), validate.OneOf(["sesame", "potato", "wheat"])])
    patty = fields.Str(required=True, validate=[validate.Length(min=1), validate.OneOf(["beef", "chicken", "veggie"])])
    sauce = fields.Str(required=False)
    toppings = fields.List(fields.String(), required=False)
