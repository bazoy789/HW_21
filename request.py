from art import aprint


class Request:
    def __init__(self, all_storage, waybill):
        self.all_storage = all_storage

        split_list = waybill.lower().split(' ')

        self._from = split_list[4]
        self._to = split_list[6]
        self._amount = int(split_list[1])
        self._product = split_list[2]

    def move(self):
        try:
            if self._from in self.all_storage.keys() or self._to in self.all_storage.keys():
                if self.all_storage[self._from].get_items[self._product] >= self._amount:
                    if self.all_storage[self._to].get_unique_items_count <= 5 and self.all_storage[self._to].get_free_space >= self._amount:
                        aprint(artname='happy', number=3)
                        print(f'На складе ЕСТЬ нужное количество\n{"_" * 20}')

                        self.all_storage[self._from].remove(self._product, self._amount)

                        print(f'Курьер забрал {self._amount} {self._product} со {self._from}')
                        print(f'Курьер везет {self._amount} {self._product} со {self._from} в {self._to}')

                        self.all_storage[self._to].add(self._product, self._amount)

                        print(f'Курьер доставил {self._amount} {self._product} в {self._to}\n{"_"*20}')
                    else:
                        print(f'В магазин недостаточно места, попробуйте что то другое\n{"_"*20}')
                else:
                    aprint(artname='sad', number=3)
                    print(f'На складе НЕТ нужное количество\n'
                          f'Попробуйте заказать меньше\n{"_"*20}')

        except Exception:
            print('нет наименование склада')


