from base_class import BaseClass


class Shop(BaseClass):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title, count):
        if self.get_unique_items_count < 5:
            super().add(title, count)
        else:
            print(f'{"_"*20}\nВ магазин недостаточно места, попробуйте что то другое')