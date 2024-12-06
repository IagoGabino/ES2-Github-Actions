class User:
    def __init__(self, username):
        self.username = username
        self.cart = []

    def add_to_cart(self, store, item_name, quantity):
        for item in store.inventory.list_all():
            if item["name"] == item_name:
                if item["quantity"] >= quantity:
                    self.cart.append({"name": item_name, "price": item["price"], "quantity": quantity})
                    return f"Added {quantity} of {item_name} to cart"
                else:
                    raise ValueError("Insufficient quantity in inventory")
        raise ValueError("Item not found in inventory")

    def checkout(self, store):
        total = sum(item["price"] * item["quantity"] for item in self.cart)
        for item in self.cart:
            store.sell_item(item["name"], item["quantity"])
        self.cart = []
        return f"Checkout complete. Total: ${total:.2f}"
