from shop import Shop
from store import Store
from request import Request

store = Store(items={})
shop = Shop(items={})


store.get_items = {
    'тортик': 4,
    'колбаса': 3,
    'макароны': 5,
    'сок': 7,
    'сыр': 10,
    'творог': 2
}

shop.get_items = {
    'тортик': 4,
    'колбаса': 3,
    'макароны': 2,
    'сок': 4,
    'сыр': 3
}

all_storage = {
    'магазин': shop,
    'склад': store
}


def main():
    while True:
        for storage in all_storage:
            print(f'Сейчас в {storage}:\n{all_storage[storage].get_items}')

        user_input = input('Введите запрос в формате (Доставить 3 печеньки из склад в магазин)\n'
                           'Введите "стоп" или "stop" для завершения программы\n:')


        if user_input in ('стоп', 'stop'):
            break
        try:
            request = Request(all_storage=all_storage, waybill=user_input)
            request.move()
        except:
            print('Ошибка ввода')
            continue


if __name__ == '__main__':
    main()
