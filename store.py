from inventory import check_stock, add_stock, remove_stock


def sell_item():
    item = input('Введите название товара для продажи: ').strip().lower()
    quantity = int(input('Введите кольчество: '))
    stock = check_stock(item)
    if stock >= quantity:
        remove_stock(item, quantity)
    else:
        print(f'Недостаточно товара {item} для продажи. Доступно только {stock}')


def buy_item():
    item = input('Введите название товара для покупки: ').strip().lower()
    quantity = int(input('Введите кольчество: '))
    add_stock(item, quantity)


def show_inventory():
    from inventory import inventory
    print('\n Текущий инвентарь')
    for item, qty in inventory.items():
        print(f'- {item}: {qty}')
