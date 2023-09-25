
import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
total = 0

def inventory_check(inventory):
    
    global total
    print("Inventory:")
    for k,v in inventory.items():
        total += v
        if v <= 1:
            print("You have {} {} in your inventory".format(v,k))
        else:
            if k.endswith("ch"):
                print("You have {} {}es in your inventory".format(v,k))

            else:
                print("You have {} {}s in your inventory".format(v, k))

    print("Total number of the items: {}".format(total))


inventory_check(stuff)