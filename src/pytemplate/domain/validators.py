import marshmallow
from marshmallow import fields


class BurgerSchema(marshmallow.Schema):
    bread = fields.String()
    patty = fields.String()
    sauce = fields.String(required=False)
    toppings = fields.List(fields.String(), required=False)
