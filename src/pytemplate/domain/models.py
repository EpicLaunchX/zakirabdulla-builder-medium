from dataclasses import dataclass

import marshmallow

from pytemplate.domain.validators import BurgerSchema


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: str | None = None
    toppings: list[str] | None = None

    def __str__(self):
        return f"{self.bread} {self.patty} {self.sauce if self.sauce else 'no sauce'} { ','.join(self.toppings) if self.toppings else 'no toppings'}"


def burger_factory(bread: str = None, patty: str = None, sauce: str | None = None, toppings: list[str] | None = None) -> Burger:
    data = {
        "bread": bread,
        "patty": patty,
        "sauce": sauce,
        "toppings": toppings,
    }
    try:
        validated_data = BurgerSchema().load(data)
    except marshmallow.ValidationError as err:
        raise marshmallow.ValidationError(err.messages) from err
    return Burger(**validated_data)
