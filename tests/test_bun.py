
class TestBun:
    def test_bun_has_name(self, get_bun):
        assert get_bun.name == "Test Bun"

    def test_bun_has_price(self, get_bun):
        assert get_bun.price == 10.5
