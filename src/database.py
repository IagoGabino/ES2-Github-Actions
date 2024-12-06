class SimpleDatabase:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)
        return item

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)
            return item
        raise ValueError("Item not found in database")

    def list_all(self):
        return self.data
