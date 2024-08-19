from marshmallow import fields, Schema


class BurgerSchema(Schema):
    bread = fields.String()
    patty = fields.String()
    sauce = fields.String(required=False)
    toppings = fields.List(fields.String(), required=False)
