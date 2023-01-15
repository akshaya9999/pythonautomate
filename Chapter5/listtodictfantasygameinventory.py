def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory.setdefault(i,1)
    return inventory

def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(v,' ',k)
        item_total+=v   
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv =addToInventory(inv, dragonLoot)
displayInventory(inv)