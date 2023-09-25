total = 0


def inventory_check(inventory):
    global total
    print("Inventory:")
    for k, v in inventory.items():
        total += v
        if v <= 1:
            print("You have {} {} in your inventory".format(v, k))
        else:
            if k.endswith("ch"):
                print("You have {} {}es in your inventory".format(v, k))

            else:
                print("You have {} {}s in your inventory".format(v, k))

    print("Total number of the items: {}".format(total))


def add_to_inventory(inventory, added_items):

    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1

        else:
            inventory.setdefault(item,1)

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', "match", "match"]
inv = add_to_inventory(inv, dragon_loot)


inventory_check(inv)