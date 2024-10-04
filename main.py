from store import sell_item, buy_item, show_inventory
from inventory_manager import manage_stock


def main():
    while True:
        print('1. Продать товар')
        print('2. Купить товар')
        print('3. Просмотреть инвентарь')
        print('4. Управление записями')
        print('5. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':
            sell_item()

        elif choice == '2':
            buy_item()

        elif choice == '3':
            show_inventory()

        elif choice == '4':
            item = input('Введите название товара: ').strip().lower()
            quantity = int(input('Введите корректоровку кольчества (может быть отрицательной): '))
            manage_stock(item, quantity)

        elif choice == '5':
            print('До свидания')
            break

        else:
            print('Неверный ввод. Пробуйте снова')


main()


