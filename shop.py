from base_class import BaseClass


class Shop(BaseClass):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)