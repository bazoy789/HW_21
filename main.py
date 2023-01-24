from shop import Shop
from store import Store
from request import Request
from art import aprint, tprint

store = Store(items={})
shop = Shop(items={})


store.get_items = {
    'тортик': 20,
    'колбаса': 20,
    'макароны': 20,
    'сок': 20,
    'сыр': 10,
    'творог': 9
}

shop.get_items = {
    'тортик': 5,
    'колбаса': 5,
    'макароны': 5,
    'сок': 2,
    'сыр': 2
}

all_storage = {
    'магазин': shop,
    'склад': store
}


def main():
    while True:
        for storage in all_storage:
            print(f'Сейчас в {storage}:\n{all_storage[storage].get_items}')
        tprint('Start working')
        user_input = input('Введите запрос в формате (Доставить 2 тортик из склад в магазин)\n'
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
