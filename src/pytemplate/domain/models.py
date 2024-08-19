from dataclasses import dataclass

from .validators import BurgerSchema


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: str | None = None
    toppings: list[str] | None = None

    def __str__(self):
        return f"{self.bread} {self.patty} {self.sauce if self.sauce else 'no sauce'} { ','.join(self.toppings) if self.toppings else 'no toppings'}"


def burger_factory(bread: str, patty: str, sauce: str | None = None, toppings: list[str] | None = None) -> Burger:
    BurgerSchema().load({"bread": bread, "patty": patty, "sauce": sauce, "toppings": toppings})
    return Burger(bread=bread, patty=patty, sauce=sauce, toppings=toppings)
