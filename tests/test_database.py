import pytest


class TestDatabase:
    def test_available_buns(self, get_database):
        assert len(get_database.available_buns())

    def test_available_ingredients(self, get_database):
        assert len(get_database.available_ingredients())
