from src.database import SimpleDatabase

class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = SimpleDatabase()

    def add_item(self, item_name, price, quantity):
        item = {"name": item_name, "price": price, "quantity": quantity}
        self.inventory.add(item)
        return item

    def sell_item(self, item_name, quantity):
        for item in self.inventory.list_all():
            if item["name"] == item_name:
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    return f"Sold {quantity} of {item_name}"
                else:
                    raise ValueError("Insufficient quantity in inventory")
        raise ValueError("Item not found in inventory")
