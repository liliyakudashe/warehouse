# inventory.py
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}

def check_stock(item):
    """Возвращает количество указанного товара на складе."""
    return inventory.get(item, 0)

def add_stock(item, quantity):
    """Добавляет указанное количество товара в инвентарь."""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"{quantity} {item} добавлено в инвентарь.")

def remove_stock(item, quantity):
    """Уменьшает количество товара на складе, если это возможно."""
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"{quantity} {item} продано.")
        if inventory[item] == 0:
            del inventory[item]
    else:
        print(f"Недостаточно {item} в инвентаре для продажи.")