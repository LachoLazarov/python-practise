#"Create a dict that tracks the amount (count) of each element on the `items` list.
# :param items: list - list of items to create an inventory from.
# :return: dict - the inventory dictionary.

fruit_list = [
    "apple", "banana", "plum", "apple", "apricot", "apple",
    "orange", "banana", "apple", "apricot", "banana", "plum",
    "banana", "apple", "plum"
]

def fruit_inventory(items):
    inventory = {}

    for fruit in items:
        if fruit not in inventory:
            inventory[fruit] = 1

        else:
            inventory[fruit] += 1

    return inventory

inventory_dict = fruit_inventory(fruit_list)
print(inventory_dict)
