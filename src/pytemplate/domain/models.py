from dataclasses import dataclass


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: str = None
    toppings: list[str] = None

    def __str__(self):
        return f"{self.bread} {self.patty} {self.sauce if self.sauce else 'no sauce'} { ','.join(self.toppings) if self.toppings else 'no toppings'}"
