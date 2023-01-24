from abstract_storage import Storage
from typing import Dict


class BaseClass(Storage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, title: str, count: int):
        if self.get_free_space >= int(count):
            self._items[title] = self._items.get(title, 0) + int(count)
        else:
            print('превышение лимита')

    def remove(self, title: str, count: int):
        if self._items[title] > int(count):
            self._items[title] = self._items.get(title, 0) - int(count)
        elif self._items[title] < int(count):
            self._items[title] = self._items.get(title, 0) - int(self._items[title])
            if self._items == 0:
                self._items.pop(title)

    @property
    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    @property
    def get_items(self):
        return self._items

    @get_items.setter
    def get_items(self, new_items):
        self._items = new_items

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())