import marshmallow
import pytest

from src.pytemplate.domain.validators import BurgerSchema


def test_burger_schema_valid_data():
    data = {"bread": "sesame", "patty": "beef", "sauce": "ketchup", "toppings": ["lettuce", "tomato"]}
    try:
        BurgerSchema().load(data)
    except marshmallow.ValidationError as e:
        pytest.fail("ValidationError raised unexpectedly!")


def test_burger_schema_missing_bread():
    data = {"bread": "", "patty": "beef", "sauce": "ketchup", "toppings": ["lettuce", "tomato"]}
    with pytest.raises(marshmallow.ValidationError) as e:
        BurgerSchema().load(data)
    assert "Bread is required" in str(e.value)


def test_burger_schema_missing_patty():
    data = {"bread": "sesame", "patty": "", "sauce": "ketchup", "toppings": ["lettuce", "tomato"]}
    with pytest.raises(marshmallow.ValidationError) as e:
        BurgerSchema().load(data)
    assert "Patty is required" in str(e.value)


def test_burger_schema_optional_fields():
    data = {"bread": "sesame", "patty": "beef"}
    try:
        validated_data = BurgerSchema().load(data)
    except marshmallow.ValidationError as e:
        pytest.fail(f"Validation error: {e.messages}")
