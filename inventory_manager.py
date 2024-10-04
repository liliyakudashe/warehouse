def manage_stock(item, adj):
    from inventory import inventory
    def update_inventory():
        nonlocal inventory
        if item in inventory:
            inventory[item] += adj
            print(f'{adj} {item} добавлено в инвентарь')
        else:
            print(f'{item} не найдено в инвенторе')

    update_inventory()
