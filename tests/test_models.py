import pytest
from marshmallow import ValidationError

from src.pytemplate.domain.models import Burger, burger_factory


def test_create_burger_with_all():
    burger = Burger(bread="sesame", patty="beef", sauce="ketchup", toppings=["lettuce", "tomato"])
    assert burger.bread == "sesame"
    assert burger.patty == "beef"
    assert str(burger) == "sesame beef ketchup lettuce,tomato"


def test_create_burger_with_no_toppings():
    burger = Burger(bread="sesame", patty="beef", sauce="ketchup", toppings=None)
    assert burger.bread == "sesame"
    assert burger.patty == "beef"
    assert str(burger) == "sesame beef ketchup no toppings"


def test_create_burger_with_no_sauce():
    burger = Burger(bread="sesame", patty="beef", toppings=["lettuce", "tomato"], sauce=None)
    assert burger.bread == "sesame"
    assert burger.patty == "beef"
    assert str(burger) == "sesame beef no sauce lettuce,tomato"


def test_burger_factory_valid():
    result = burger_factory("sesame", "beef", "ketchup", ["lettuce", "tomato"])
    assert result.bread == "sesame"
    assert isinstance(result, Burger)
    assert str(result) == "sesame beef ketchup lettuce,tomato"


def test_burger_factory_invalid():
    with pytest.raises(ValidationError):
        burger_factory(1, "beef", "ketchup", "lettuce,tomato")

    with pytest.raises(ValidationError):
        burger_factory("sesame", "beef", 1, "lettuce,tomato")
