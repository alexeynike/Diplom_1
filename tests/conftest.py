import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database


@pytest.fixture
def get_bun():
    return Bun("Test Bun", 10.5)


@pytest.fixture
def get_burger():
    return Burger()

@pytest.fixture
def get_ingredient():
    return Ingredient(ingredient_type="Sauce", name="Cheese Sauce", price=1.5)

@pytest.fixture
def add_ingredient():
    def wrapper(ingredient_type, name, price):
        return Ingredient(ingredient_type, name, price)
    return wrapper

@pytest.fixture
def add_bun():
    def wrapper(name, price):
        return Bun(name, price)
    return wrapper

@pytest.fixture
def get_database():
    return Database()