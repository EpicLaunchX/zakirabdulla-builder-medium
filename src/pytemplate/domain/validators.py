import marshmallow


class BurgerSchema(marshmallow.Schema):
    bread = marshmallow.fields.Str(required=True)
    patty = marshmallow.fields.Str(required=True)
    sauce = marshmallow.fields.Str(required=False, allow_none=True)
    toppings = marshmallow.fields.List(marshmallow.fields.Str(), required=False, allow_none=True)

    @marshmallow.validates("bread")
    def validate_bread(self, value):
        if not value:
            raise marshmallow.ValidationError("Bread is required")

    @marshmallow.validates("patty")
    def validate_patty(self, value):
        if not value:
            raise marshmallow.ValidationError("Patty is required")
