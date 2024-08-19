import marshmallow
from marshmallow import fields


class BurgerSchema(marshmallow.Schema):
    bread = fields.String(required=True)
    patty = fields.String(required=True)
    sauce = fields.String(required=False)
    toppings = fields.List(fields.String(), required=False)
