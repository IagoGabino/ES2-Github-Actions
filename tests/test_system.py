import unittest
from src.store import Store
from src.user import User

class TestStoreSystem(unittest.TestCase):
    def setUp(self):
        self.store = Store("Sports Store")
        self.user = User("Iago Gabino")
        self.store.add_item("Football", 20.0, 10)
        self.store.add_item("Basketball", 25.0, 5)

    def test_add_item(self):
        item = self.store.add_item("Tennis Racket", 50.0, 3)
        self.assertIn(item, self.store.inventory.list_all())

    def test_sell_item(self):
        self.assertEqual(self.store.sell_item("Football", 2), "Sold 2 of Football")
        for item in self.store.inventory.list_all():
            if item["name"] == "Football":
                self.assertEqual(item["quantity"], 8)

    def test_add_to_cart(self):
        self.assertEqual(self.user.add_to_cart(self.store, "Football", 2), "Added 2 of Football to cart")
        self.assertEqual(len(self.user.cart), 1)

    def test_checkout(self):
        self.user.add_to_cart(self.store, "Football", 2)
        total = self.user.checkout(self.store)
        self.assertIn("Total: $40.00", total)
        self.assertEqual(len(self.user.cart), 0)

if __name__ == "__main__":
    unittest.main()
