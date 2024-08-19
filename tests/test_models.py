import marshmallow
import pytest

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


def test_burger_factory_valid_data():
    data = {"bread": "sesame", "patty": "beef", "sauce": "ketchup", "toppings": ["lettuce", "tomato"]}
    burger = burger_factory(data)
    assert isinstance(burger, Burger)
    assert str(burger) == "sesame beef ketchup lettuce,tomato"
    assert burger.bread == "sesame"
    assert burger.patty == "beef"
    assert burger.sauce == "ketchup"
    assert burger.toppings == ["lettuce", "tomato"]


def test_burger_factory_missing_bread():
    data = {"patty": "beef", "sauce": "ketchup", "toppings": ["lettuce", "tomato"]}
    with pytest.raises(marshmallow.ValidationError) as e:
        burger_factory(data)


def test_burger_factory_missing_patty():
    data = {"bread": "sesame", "sauce": "ketchup", "toppings": ["lettuce", "tomato"]}
    with pytest.raises(marshmallow.ValidationError) as e:
        burger_factory(data)


def test_burger_factory_optional_fields():
    data = {"bread": "sesame", "patty": "beef"}
    burger = burger_factory(data)
    assert isinstance(burger, Burger)
    assert str(burger) == "sesame beef no sauce no toppings"
    assert burger.bread == "sesame"
    assert burger.patty == "beef"
    assert burger.sauce is None
    assert burger.toppings is None
