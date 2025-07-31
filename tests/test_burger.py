
class TestBurger:
    def test_create_default_burger(self, get_burger):
        assert get_burger.bun is None
        assert get_burger.ingredients == []

    def test_add_bun(self, get_burger, get_bun):
        burger = get_burger
        burger.set_buns(get_bun)
        assert burger.bun is not None

    def test_add_ingredient(self, get_burger, get_ingredient):
        burger = get_burger
        burger.add_ingredient(get_ingredient)
        assert len(burger.ingredients) > 0

    def test_remove_ingredient(self, get_burger, get_ingredient):
        burger = get_burger
        burger.add_ingredient(get_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, get_burger, add_ingredient):
        ingredient_1 = add_ingredient("Cheese", "Cheder", 2.3)
        ingredient_2 = add_ingredient("Sauce", "Cheese cause", 1.5)
        burger = get_burger
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.ingredients == [ingredient_1, ingredient_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_check_burger_price(self, get_burger, add_ingredient, add_bun):
        burger = get_burger
        ingredient_1 = add_ingredient("Cheese", "Cheder", 2.3)
        ingredient_2 = add_ingredient("Sauce", "Cheese cause", 1.5)
        bun = add_bun("Small bun", 2.5)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == ingredient_1.price + ingredient_2.price + (bun.price * 2)
