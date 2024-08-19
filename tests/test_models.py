import pytest

from src.pytemplate.domain.models import Burger


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
