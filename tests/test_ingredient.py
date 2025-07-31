class TestIngredient:
    def test_price(self, add_ingredient):
        ingredient = add_ingredient("Sauce", "Cheese", 2.5)
        assert ingredient.price == 2.5

    def test_name(self, get_ingredient):
        assert get_ingredient.name == "Cheese Sauce"

    def test_type(self, get_ingredient):
        assert get_ingredient.type == "Sauce"
